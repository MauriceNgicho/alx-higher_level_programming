#!/usr/bin/python3
"""
A script that takes GitHub credentials (username and personal access token)
and uses the GitHub API to display the user's id.
"""

import requests
import sys

if __name__ == "__main__":
    # Get the username and personal access token from command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]

    # GitHub API URL
    url = "https://api.github.com/user"

    # Send a GET request with Basic Authentication
    response = requests.get(url, auth=(username, password))

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        json_data = response.json()
        print(json_data.get("id"))
    else:
        # Print None if authentication fails or an error occurs
        print("None")
