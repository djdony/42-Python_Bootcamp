import sys

args = sys.argv


def print_usage():
    print()
    print("Usage: python operations.py <number1> <number2>")
    print('Example:')
    print('    python operations.py 10 3')


def operations(num1, num2):
    print('Sum :{}'.format(num1 + num2))
    print('Difference :{}'.format(num1 - num2))
    print('Product :{}'.format(num1 * num2))
    if num2 == 0:
        print('Quotient: ERROR (div by zero)')
        print('Quotient: ERROR (modulo by zero)')
    else:
        print('Quotient :{}'.format(num1 / num2))
        print('Remainder :{}'.format(num1 % num2))

try:
    num1 = int(args[1])
    num2 = int(args[2])
    if 1 < len(args) == 3:
        operations(num1, num2)
    elif len(args) > 2:
        print('InputError: too many arguments')
        print_usage()
    else:
        print("ERROR")
except ValueError:
    print("InputError: only numbers")
    print_usage()

except Exception:
    print_usage()





