
from sys import argv

MORSE = {
    'A': '.-',    'B': '-...',  'C': '-.-.',  'D': '-..',   'E': '.', 
    'F': '..-.',  'G': '--.',   'H': '....',  'I': '..',    'J': '.---', 
    'K': '-.-',   'L': '.-..',  'M': '--',    'N': '-.',    'O': '---', 
    'P': '.--.',  'Q': '--.-',  'R': '.-.',   'S': '...',   'T': '-', 
    'U': '..-',   'V': '...-',  'W': '.--',   'X': '-..-',  'Y': '-.--', 
    'Z': '--..',  ' ': '/',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', 
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'
}

def main() -> None:
    if len(argv) != 2:
        print("AssertionError: the arguments are bad")
        return
    text: str = argv[1].upper()
    try:
        print(" ".join([MORSE[c] for c in text]))
    except KeyError:
        print("AssertionError: the arguments are bad")


if __name__ == '__main__':
    main()
