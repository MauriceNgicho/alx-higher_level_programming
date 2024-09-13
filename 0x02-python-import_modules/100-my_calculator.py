#!/usr/bin/python3
if __name__ == "__main__":

    # Importing all the necessary functions from calculator_1.py
    from calculator_1 import add, sub, mul, div
    import sys

    # Check if the number of arguments is correct
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    # Get the arguments from the command line
    a = int(sys.argv[1])  # Convert the first argument to an integer
    operator = sys.argv[2]  # The operator
    b = int(sys.argv[3])  # Convert the third argument to an integer

    # Perform the operation based on the operator
    if operator == '+':
        result = add(a, b)
    elif operator == '-':
        result = sub(a, b)
    elif operator == '*':
        result = mul(a, b)
    elif operator == '/':
        result = div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    print("{} {} {} = {}".format(a, operator, b, result))
