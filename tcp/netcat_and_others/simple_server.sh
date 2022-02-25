#!/bin/bash
read MESSAGE
# spaces are the default delimiter, but we're being explicit here
IFS=' ' read -r -a MESSAGE_ARRAY <<< "$MESSAGE"
HTTP_METHOD=${MESSAGE_ARRAY[0]}
ENDPOINT=${MESSAGE_ARRAY[1]}
if [[ "$ENDPOINT" == "/hi" ]]; then
  RESPONSE="oh hi"
else 
  RESPONSE="not found!"
fi
echo "HTTP/1.1 200\n$RESPONSE"
