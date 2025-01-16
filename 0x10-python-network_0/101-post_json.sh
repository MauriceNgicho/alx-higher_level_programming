#!/bin/bash
# A Bash script that sends a JSON POST request to a URL using a file as the request body
curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1"
