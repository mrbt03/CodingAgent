from functions.run_python_file import run_python_file

def test_run_python_file():
    print(f"Result for main.py: {run_python_file("calculator", "main.py")}\n")
    print(f"Result for main.py with args: {run_python_file("calculator", "main.py", ["3 + 5"])}\n")
    print(f"Result for calculator tests: {run_python_file("calculator", "tests.py")}\n")
    print(f"Result for main.py in parent: {run_python_file("calculator", "../main.py")}\n")
    print(f"Result for nonexistent.py: {run_python_file("calculator", "nonexistent.py")}\n")
    print(f"Result for lorem.txt: {run_python_file("calculator", "lorem.txt")}\n")

if __name__ == "__main__":
    test_run_python_file()