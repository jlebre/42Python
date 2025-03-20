import sys

NESTED_MORSE = {
    " ": "/ ",
    "A": ".- ",
    "B": "-... ",
    "C": "-.-. ",
    "D": "-.. ",
    "E": ". ",
    "F": "..-. ",
    "G": "--. ",
    "H": ".... ",
    "I": ".. ",
    "J": ".--- ",
    "K": "-.- ",
    "L": ".-.. ",
    "M": "-- ",
    "N": "-. ",
    "O": "--- ",
    "P": ".--. ",
    "Q": "--.- ",
    "R": ".-. ",
    "S": "... ",
    "T": "- ",
    "U": "..- ",
    "V": "...- ",
    "W": ".-- ",
    "X": "-..- ",
    "Y": "-.-- ",
    "Z": "--.. ",
    "0": "----- ",
    "1": ".---- ",
    "2": "..--- ",
    "3": "...-- ",
    "4": "....- ",
    "5": "..... ",
    "6": "-.... ",
    "7": "--... ",
    "8": "---.. ",
    "9": "----. "
}


def main():
    """
    Main
    """

    argv = sys.argv

    if not parse(argv):
        raise AssertionError("the arguments are bad")

    phrase = argv[1].upper()
    morse = ""

    for c in phrase:
        morse += NESTED_MORSE[c]

    print(morse)


def parse(argv):
    """
    Parse function
    """
    if len(argv) != 2:
        return False
    if not all(c.isalnum() or c.isspace() for c in argv[1]):
        return False
    return True


if __name__ == "__main__":
    main()
