#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        # If division by zero occurs, return None
        result = None
    finally:
        # Print the result in the finally block
        print("Inside result: {}".format(result))
    return result
