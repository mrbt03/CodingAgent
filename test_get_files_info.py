from functions.get_files_info import get_files_info

def test_get_files_info():
    print(f"Result for current directory: {get_files_info("calculator",".")}\n")
    print(f"Result for pkg directory: {get_files_info("calculator", "pkg")}\n")
    print(f"Result for bin directory: {get_files_info("calculator", "/bin")}\n")
    print(f"Result for parent directory: {get_files_info("calculator", "../")}\n")

if __name__ == "__main__":
    test_get_files_info()