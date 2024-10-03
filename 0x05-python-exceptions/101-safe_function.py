#!/usr/bin/python3
import sys

def safe_function(fct, *args):
    """
    Executes a function safely.
    
    Parameters:
    - fct: a function to execute
    - *args: arguments to pass to the function
    
    Returns:
    - The result of the function if no error occurs.
    - None if an exception is raised, and prints the exception message.
    """
    try:
        # Attempt to execute the function with the given arguments
        return fct(*args)
    except Exception as e:
        # If an exception occurs, print the error message to stderr
        print("Exception: {}".format(e), file=sys.stderr)
        return None
