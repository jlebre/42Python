import sys

try:
    assert len(sys.argv) == 2, "more than one argument is provided"

    num = sys.argv[1]

    try:
        num = int(num)
    except ValueError:
        raise AssertionError("argument is not an integer")


    if num % 2 == 0 or num == 0:
        print("I'm Even")
    else:
        print("I'm Odd")
except AssertionError as error:
    print(f"AssertionError: {error}")
    sys.exit(1)

# The subject says print an AssertionError
# Can be interpreted as RAISE an exception
# Or simply print the message
# So I did both

'''
Nargs = len(sys.argv)
if Nargs > 2:
    print("AssertionError: more than one argument is provided")
elif Nargs == 2:
    num = sys.argv[1]

    try:
        num = int(num)
    except ValueError:
        print("AssertionError: argument is not an integer")

    if num % 2 == 0 or num == 0:
        print("I'm Even")
    else:
        print("I'm Odd")
'''

