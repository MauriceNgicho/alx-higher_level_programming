#!/usr/bin/python3
"""
This script takes in a URL and an email address,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8).
"""

import urllib.parse
import urllib.request
import sys

if __name__ == "__main__":
    # Get URL and email from command-line arguments
    url = sys.argv[1]
    email = sys.argv[2]

    # Create the data dictionary with the email
    data = {'email': email}

    # Encode the data to be sent as POST parameters
    encoded_data = urllib.parse.urlencode(data).encode('utf-8')

    # Send the POST request
    with urllib.request.urlopen(url, data=encoded_data) as response:
        # Read and decode the body of the response
        body = response.read().decode('utf-8')
        print(body)
