
from ft_filter import ft_filter
from sys import argv

def main() -> None:
    if len(argv) != 3 or not argv[2].isdigit():
        print('AssertionError: the arguments are bad')
        return

    print(ft_filter(lambda s : len(s) >= int(argv[2]), argv[1].split()))

if __name__ == '__main__':
    main()

