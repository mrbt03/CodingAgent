from functions.get_file_content import get_file_content

def test_get_files_content():
    print(f"Result for main.py: {get_file_content("calculator","main.py")}\n")
    print(f"Result for lorem.txt: {len(get_file_content("calculator","lorem.txt"))}\n")
    print(f"Result for pkg/calculator.py: {get_file_content("calculator", "pkg/calculator.py")}\n")
    print(f"Result for bin/cat: {get_file_content("calculator", "/bin/cat")}\n")
    print(f"Result for pkg/does_not_exist.py: {get_file_content("calculator", "pkg/does_not_exist.py")}\n")

if __name__ == "__main__":
    test_get_files_content()