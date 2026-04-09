import os
from dotenv import load_dotenv
from google import genai
import argparse
from google.genai import types


def main():
    print("Hello from codingagent!")
    load_dotenv()
    try:
        api_key = os.environ.get("GEMINI_API_KEY")
    except KeyError:
        raise RuntimeError("Gemini API key is not set")

    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()
    
    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents = messages)
    try:
        if args.verbose:
            if not response.usage_metadata:
                raise RuntimeError("Response usage metadata is not set")
            user_prompt = args.user_prompt
            prompt_tokens = response.usage_metadata.prompt_token_count
            response_tokens = response.usage_metadata.candidates_token_count
            print(f"User prompt: {user_prompt}\nPrompt tokens: {prompt_tokens}\nResponse tokens: {response_tokens}")
        print(f"Response:\n{response.text}")
    except Exception as e:
        raise RuntimeError(f"Error: {e}")



if __name__ == "__main__":
    main()
