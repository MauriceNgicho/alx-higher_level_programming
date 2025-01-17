#!/usr/bin/python3
import urllib.request


url = "https://alx-intranet.hbtn.io/status"

if __name__ == "__main__":
    with urllib.request.urlopen(url) as response:
        body = response.read()
        print("Body response:")
        print("- type: {}".format(type(body)))
        print("- content: {}".format(body))
        print("- utf8 content: {}".format(body.decode('utf-8')))
