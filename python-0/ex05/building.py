
from string import punctuation
from sys import argv

def main() -> None:
    if len(argv) > 2:
        print("AssertionError: too many arguments")
        return
    text: str = argv[1] if len(argv) == 2 else input("What is the text to count?\n")

    a = filter(lambda x : x.isalpha(), text)

    print(f"The text contains {len(text)} characters:")
    print(f"{len(list(filter(lambda c : c.isupper(), text)))} upper letters")
    print(f"{len(list(filter(lambda c : c.islower(), text)))} lower letters")
    print(f"{len(list(filter(lambda c : c in punctuation, text)))} punctuation marks")
    print(f"{len(list(filter(lambda c : c.isspace(), text)))} spaces")
    print(f"{len(list(filter(lambda c : c.isdigit(), text)))} digits")

if __name__ == '__main__':
    main()
