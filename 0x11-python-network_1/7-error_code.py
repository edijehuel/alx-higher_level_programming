#!/usr/bin/python3
""" Python script that takes in a URL,
    sends a request to the URL and displays the body of the response
"""
import requests
from sys import argv


if __name__ == "__main__":
    response = requests.get(argv[1])
    if response:
        print(response.text)
    else:
        print("Error code: {}".format(response.status_code))
