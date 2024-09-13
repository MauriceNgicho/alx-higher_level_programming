#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    total = 0   # Initialize sum to zero

    # Loop through the arguments skiping thr first on(the script name)
    for arg in sys.argv[1:]:
        total += int(arg)
    print(total)
