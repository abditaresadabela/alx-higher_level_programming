#!/bin/bash

# Check if a URL is provided as an argument
if [ -z "$1" ]; then
    echo "Please provide a URL as an argument"
    exit 1
fi

# Send a GET request to the provided URL using curl
response=$(curl -s -o /dev/null -w "%{http_code}" "$1")
if [[ "$response" == "200" ]]; then
    body=$(curl -s "$1")
    echo "$body"
else
    echo "The server returned a status code of $response"
fi
