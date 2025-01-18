#!/usr/bin/python3
"""
script that takes in a URL and an email address,
sends a POST request to the passed URL with the email as a parameter,
and finally displays the body of the response.
"""
import requests
import sys

if __name__ == "__main__":

    # Get url and email from the command line
    url = sys.argv[1]
    email = sys.argv[2]

    # payload to send the post request
    payload = {"email": email}

    # Send post request
    response = requests.post(url, data=payload)

    # Print
    print(response.text)
