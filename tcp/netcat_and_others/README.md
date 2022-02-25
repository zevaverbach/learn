Trying to understand what's happening at a somewhat low level with TCP, let's look at Julia Evans's zines about related topics.

# TODO
- [ ] return the contents of files, if they exist, according to the endpoint
- [ ] dynamically generate the content based on the endpoint/params
- [ ] do some sort of auth, including maybe JWTs or sessions
- [ ] support POST requests
- [ ] do some infosec
- [ ] port to Python or Rust

# Resources
- https://www.varonis.com/blog/netcat-commands
- https://infosecwriteups.com/mastering-ncat-for-fun-and-profit-397e982b889c
- https://www.youtube.com/watch?v=VF4In6rIPGc
- [`ncat --broker`](https://stackoverflow.com/a/47865255)

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
read MESSAGE
IFS=' ' read -r -a MESSAGE_ARRAY <<< "$MESSAGE"
HTTP_METHOD=${MESSAGE_ARRAY[0]}
ENDPOINT=${MESSAGE_ARRAY[1]}
if [[ "$ENDPOINT" == "/hi" ]]; then
  RESPONSE="oh hi"
else 
  RESPONSE="not found!"
fi
echo "HTTP/1.1 200 $RESPONSE"
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
> User-Agent: curl/7.77.0
> Accept: */*
> 
* Mark bundle as not supporting multiuse
< HTTP/1.1 200 not found!
* Connection #0 to host <IP> left intact
```
