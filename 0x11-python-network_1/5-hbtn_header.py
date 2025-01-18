#!/usr/bin/python3
"""
A script that takes in a URL, sends a request to it,
and displays the value of the X-Request-Id variable
found in the response header
"""
import requests
import sys

if __name__ == "__main__":

    url = sys.argv[1]

    # Get the url from the command line
    response = requests.get(url)

    # Retrieve and print the header value.
    print(response.headers.get("X-Request-Id"))
