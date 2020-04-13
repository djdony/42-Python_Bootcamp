import sys

args = sys.argv


try:
    num = int(args[1])
    if 1 < len(args) == 2:
        if num == 0:
            print("I'm Zero.")
        elif num % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")
    else:
        print("ERROR")
except ValueError:
    print("ERROR")
except IndexError:
    pass
