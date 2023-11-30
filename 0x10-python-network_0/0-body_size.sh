#!/usr/bin/env bash
# Send a request to a URL and display the size of the body of the response in bytes.
# Usage: ./0-body_size.sh <URL>

if [ $# -lt 1 ]; then
    echo "Usage: ./0-body_size.sh <URL>"
    exit 1
else
   curl -sI "$1" | grep Content-Length | cut --delimiter=" " -f 2
fi
