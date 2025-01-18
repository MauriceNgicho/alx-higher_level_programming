#!/usr/bin/python3
"""
A script that takes in a URL, sends a request to the URL
and displays the body of the response.
"""
import requests
import sys

if __name__ == "__main__":
    # Get url from command line
    url = sys.argv[1]

    # Send get request
    response = requests.get(url)

    # Check if the status code indicates an error
    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)
