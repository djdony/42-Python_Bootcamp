import sys

args = sys.argv


def reverse(s):
    return s[::-1]


for arg in reversed(args[1:]):
    print(reverse(arg), end=' ')
