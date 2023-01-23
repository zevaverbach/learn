Trying to understand what's happening at a somewhat low level with TCP, let's look at Julia Evans's zines about related topics.

# TODO
- [ ] read through [this](https://nivethan.dev/devlog/a-web-server-in-bash.html), which is a very similar adventure to ours.
    - it uses `netcat` with a `--keep-open` flag instead of switching to `socat`
    - [repo](https://github.com/Krowemoh/bash-server)
- [ ] return the contents of files, if they exist, according to the endpoint
- [ ] dynamically generate the content based on the endpoint/params
- [ ] do some sort of auth, including maybe JWTs or sessions
- [ ] support POST requests
- [ ] do some infosec
- [ ] see TODOs in simple_server.sh
- [ ] look at `netcat.c` and `netcat.h`, see if you can decipher what's happening
- [ ] figure out why `socat` isn't the right tool for making a production webserver
  - as claimed [https://stackoverflow.com/a/9621880/4386191](here) ("socat's use of fork() rather than something more sophisticated like preforking or connection pooling is the reason you wouldn't want to implement high-performance middleware with socat!")
- [ ] related to the above: what is a pre-fork web server?
    - [some material](https://stackoverflow.com/questions/25834333/what-exactly-is-a-pre-fork-web-server-model#:~:text=Pre%2Dforking%20basically%20means%20a,before%20a%20request%20comes%20in.)
- [ ] connect the dots between this basic web server and
  - [ ] gunicorn
  - [ ] werkzeug
  - [ ] flask
  - [ ] nginx

# Netcat
Start a server!
```bash
> nc -l <PORT>
```

Open another terminal window and curl the server:

```bash
> curl localhost:<PORT>
```

The `nc` terminal shows this
```bash
GET / HTTP/1.1
Host: localhost:7890
User-Agent: curl/7.77.0
Accept: */*
```

The curl session shows no additional output and stays open. When I `ctrl-c` out of the session, the `nc` session also ends, displaying

```bash
curl: (52) Empty reply from server
```

A quick `man curl` shows that the `-v` flag will give us verbose output. `man nc` gives us the `-k` flag which "Forces nc to stay listening for another connection after its current connection is completed...".

Thus, running `nc -l -k 7890` and `curl -v localhost:7890` makes it so the netcat server continues running after ending the curl session. curl displays:
  
```bash                                                                            
> curl -v localhost:7890                                                           
*   Trying ::1:7890...                                                             
* connect to ::1 port 7890 failed: Connection refused                              
*   Trying 127.0.0.1:7890...                                                       
* Connected to localhost (127.0.0.1) port 7890 (#0)                                
> GET / HTTP/1.1                                                                   
> Host: localhost:7890                                                             
> User-Agent: curl/7.77.0                                                          
> Accept: */*                                                                      
>
```

# `socat`
`nc` can only serve one client at a time. a little bit of Googling yields `socat` which can "multithread".

```bash
socat -v -v TCP-LISTEN:7890,crlf,fork,reuseaddr system:./simple_server.sh
```

`simple_server.sh`:

```bash
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
```

```bash
> curl -v <IP>:7890/hi
*   Trying <IP>:7890...
* Connected to <IP> (<IP>) port 7890 (#0)
> GET /hi HTTP/1.1
> Host: <IP>:7890
> User-Agent: curl/7.77.0
> Accept: */*
> 
* Mark bundle as not supporting multiuse
< HTTP/1.1 200 oh hi
* Connection #0 to host <IP> left intact
> 
> curl -v <IP>:7890/other
*   Trying <IP>:7890...
* Connected to <IP> (<IP>) port 7890 (#0)
> GET /hi HTTP/1.1
> Host: <IP>:7890
> User-Agent: curl/7.79.1
> Accept: */*
> 
* Mark bundle as not supporting multiuse
< HTTP/1.1 200 OK
< Content-Type: text/html; charset=utf-8
< Content-Length: 8
< 
* Connection #0 to host 165.232.110.37 left intact
Hi There
```
