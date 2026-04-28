import os
from dotenv import load_dotenv
from google import genai
import argparse
from google.genai import types
from prompts import system_prompt
from call_function import available_functions, call_function


def main():
    # Load env variables
    load_dotenv()
    try:
        api_key = os.environ.get("GEMINI_API_KEY")
    except KeyError:
        raise RuntimeError("Gemini API key is not set")

    # Define parser for cli arguments
    parser = argparse.ArgumentParser(description="Chatbot")
    # Add user prompt arguement
    parser.add_argument("user_prompt", type=str, help="User prompt")

    # Add verbose flag arguement
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")

    # Parse arguments
    args = parser.parse_args()
    
    # Define messages for Gemini client
    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

    # Initialize Gemini client
    client = genai.Client(api_key=api_key)
    try:
        # Generate response with 2.5 flash using messages
        max_iterations = 20
        for i in range(max_iterations):
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents = messages,
                config=types.GenerateContentConfig(tools=[available_functions],system_instruction=system_prompt, temperature=0))
            for candidate in response.candidates:
                if candidate.content:
                    messages.append(candidate.content)
                
                # If verbose flag set, print verbose output
            if args.verbose:
                # Error if response usage metadata is not set
                if not response.usage_metadata:
                    raise RuntimeError("Response usage metadata is not set")
                # Print user prompt, prompt token count, and response tocken count
                user_prompt = args.user_prompt
                prompt_tokens = response.usage_metadata.prompt_token_count
                response_tokens = response.usage_metadata.candidates_token_count
                print(f"User prompt: {user_prompt}\nPrompt tokens: {prompt_tokens}\nResponse tokens: {response_tokens}")
            # Print model response
            function_results = []
            function_calls = response.function_calls or []
            print(f"Function calls: {function_calls}")
            for function_call in function_calls:
                print(f"Function call: {function_call}")
                function_call_result = call_function(function_call, args.verbose)
                if not function_call_result.parts:
                    raise RuntimeError("Function call result is empty")
                if not function_call_result.parts[0].function_response.response:
                    raise RuntimeError("Function call result is not set")
                function_results.append(function_call_result.parts[0])
                if args.verbose:
                    print(f"-> {function_call_result.parts[0].function_response.response}")
                #print(f"Calling function: {function_call.name}({function_call.args})")
            if not function_calls:
                print(f"Response:\n{response.text}")
                break
            messages.append(types.Content(role="user", parts=function_results))
        else:
            print(f"Model still has not finished after {max_iterations} attempts")
            exit(1)
    # Raise exception if response cannot be generated
    except Exception as e:
        raise RuntimeError(f"Error: {e}")

if __name__ == "__main__":
    main()
