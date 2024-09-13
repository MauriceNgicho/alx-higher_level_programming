#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args_count = len(sys.argv) - 1

    # Print number of arguments
    if args_count == 0:
        print("0 arguments")
    elif args_count == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(args_count))

    # Print each args with its position
    for i in range(1, len(sys.argv)):
        print("{}: {}".format(i, sys.argv[i]))
