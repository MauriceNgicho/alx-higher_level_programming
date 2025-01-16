#!/bin/bash
# A Bash script that takes in a URL, sends a GET request with a custom header, and displays the response body
curl -sH "X-School-User-Id: 98" "$1"
