import sys

def main():
    """
    Main
    """
    argc = len(sys.argv)
    assert argc <= 2, "Too many arguments"

    if argc == 2:
        text = sys.argv[1]
    else:
        print("What is the text to count?\nHello World!")
        text = "Hello World!\r"
    
    count(text)

def count(string):
    """
    Function to count
    Upper letters
    Lower letters
    Pontuation marks
    Spaces
    Digits
    """
    Up = 0
    Lo = 0
    Pont = 0
    Spa = 0
    Digi = 0

    for char in string:
        if char.isupper():
            Up += 1
        elif char.islower():
            Lo += 1
        elif char.isspace() or char == '\r':
            Spa += 1
        elif char.isdigit():
            Digi += 1
        else:
            Pont += 1
    
    total = Up + Lo + Pont + Spa + Digi
    print(f"The text contains {total} characters")
    print(f"{Up} upper letters")
    print(f"{Lo} lower letters")
    print(f"{Pont} pontuation marks")
    print(f"{Spa} spaces")
    print(f"{Digi} digits")
    
if __name__ == "__main__":
    main()