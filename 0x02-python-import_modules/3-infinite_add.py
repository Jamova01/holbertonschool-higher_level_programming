#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    args = sys.argv[1:]
    addition = 0

    for i in args:
        addition += int(i)

    print(addition)
