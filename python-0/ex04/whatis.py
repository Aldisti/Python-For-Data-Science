from sys import argv

def main() -> int:
    if len(argv) != 2:
        print(f"AssertionError: {'more' if len(argv) > 2 else 'less'} than one argument is provided")
        return 1
    elif not argv[1].isdigit():
        print("AssertionError: argument is not an integer")
        return 1
    print("I'm Even." if int(argv[1]) % 2 == 0 else "I'm Odd.")

if __name__ == '__main__':
    exit(main())

