#!/bin/bash
# A Bash script that makes a request to 0.0.0.0:5000/catch_me to get the message "You got me!"
curl -s -L -X PUT -H "Origin: HolbertonSchool" -d "user_id=98" 0.0.0.0:5000/catch_me
