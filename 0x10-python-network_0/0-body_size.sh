#!/bin/bash
# A Bash script that takes in a URL, sends a request to that URL and show size
curl -s "$1" -o /dev/null -w '%{size_download}\n'
