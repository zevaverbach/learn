#!/bin/bash

#### INPUT
# read stdin which, when this is run with `socat`, will be an incoming request
read MESSAGE
# split the message on spaces
# spaces are the default delimiter, but we're being explicit here
IFS=' ' read -r -a MESSAGE_ARRAY <<< "$MESSAGE"
HTTP_METHOD=${MESSAGE_ARRAY[0]}
ENDPOINT=${MESSAGE_ARRAY[1]}
# TODO: check other headers, maybe even including authentication and authorization
#### /INPUT

#### OUTPUT
STATUS_LINE="HTTP/1.1 "
if [[ "$ENDPOINT" == "/hi" ]]; then
  STATUS_LINE+="200 OK"
  RESPONSE="Hi There"
else 
  STATUS_LINE+="400 NOT FOUND"
  RESPONSE=""
# TODO: produce other responses
fi

RESPONSE_LENGTH=$(echo $RESPONSE | wc -c)
# this is necessary maybe because of the omission of a newline below with 'echo -n'
# without it, this appears: "curl: (18) transfer closed with 1 bytes remaining to read"
((RESPONSE_LENGTH=RESPONSE_LENGTH-1))

echo $STATUS_LINE
echo "Content-Type: text/html; charset=utf-8"
echo "Content-Length: $RESPONSE_LENGTH"
echo ""
echo -n $RESPONSE
# TODO: add Date and Server headers, at least
#### /OUTPUT
