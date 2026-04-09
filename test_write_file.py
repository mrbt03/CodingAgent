from functions.write_file import write_file

def test_write_file():
    print(f"Result for lorem.txt: {write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")}\n")
    print(f"Result for pkg/morelorem.txt: {write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")}\n")
    print(f"Result for /tmp/temp.txt: {write_file("calculator", "/tmp/temp.txt", "this should not be allowed")}\n")

if __name__ == "__main__":
    test_write_file()