#!/usr/bin/python3
"""
A script that sends a request to a given URL and displays the body of the
response (decoded in utf-8). It also handles HTTPError exceptions.
"""

import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    try:
        # Send the request and handle the response
        with urllib.request.urlopen(url) as response:
            body = response.read()
            print(body.decode("utf-8"))
    except urllib.error.HTTPError as e:
        # Handle HTTPError and print the status code
        print(f"Error code: {e.code}")
