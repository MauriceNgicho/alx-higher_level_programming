#!/bin/bash
# A Bash script that takes in a URL, sends a POST request with specific parameters, and displays the response body
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
