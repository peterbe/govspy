import sys


def transform(*args):
    for arg in args:
        print(arg.upper())


if __name__ == "__main__":
    transform(*sys.argv[1:])
