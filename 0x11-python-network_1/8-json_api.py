#!/usr/bin/python3
"""
A script that takes in a letter as input and sends a POST request
to a url with the letter as a parameter.
"""

import requests
import sys

if __name__ == "__main__":
    # Get the letter from command-line arguments or set it to an empty string
    url = "http://0.0.0.0:5000/search_user"
    letter = sys.argv[1] if len(sys.argv) > 1 else ""

    # Create the payload with the letter
    payload = {"q": letter}

    try:
        # Send a POST request
        response = requests.post(url, data=payload)

        # Parse the response body as JSON
        json_data = response.json()

        # Check if JSON data is empty
        if json_data:
            print("[{}] {}".format(json_data.get("id"), json_data.get("name")))
        else:
            print("No result")
    except ValueError:
        # Handle invalid JSON response
        print("Not a valid JSON")
