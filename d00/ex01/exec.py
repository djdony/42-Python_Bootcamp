import sys

args = sys.argv


def reverse(s):
    str_reverse = s[::-1]
    str1 = ''
    for i in str_reverse:
        if i.isupper():
            str1 += i.lower()
        else:
            str1 += i.upper()
    return str1


for arg in reversed(args[1:]):
    print(reverse(arg), end=' ')
