import sys
from ft_filter import ft_filter


def main():
    """
    Main function
    """
    args = sys.argv

    if not parse(args):
        raise AssertionError("the arguments are bad")

    words = args[1].split()

    nb = int(args[2])

    check_len = lambda word: len(word) >= nb

    new = list(ft_filter(check_len, words))
    print(new)


def parse(argv):
    """
    Function to parse the user input
    Return False if bad
    Return True if good
    """

    if len(argv) != 3:
        return False

    try:
        int(argv[2])
    except ValueError:
        return False

    return True


if __name__ == "__main__":
    main()
