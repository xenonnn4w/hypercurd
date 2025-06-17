from functions.run_python import run_python_file

def main():
    # Test cases
    test_cases = [
        ("calculator", "main.py"),
        ("calculator", "tests.py"),
        ("calculator", "../main.py"),
        ("calculator", "nonexistent.py")
    ]

    # Run each test case
    for working_dir, file_path in test_cases:
        print(f"\nTesting: {working_dir}/{file_path}")
        result = run_python_file(working_dir, file_path)
        print(result)

if __name__ == "__main__":
    main()