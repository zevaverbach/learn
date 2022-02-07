# Why I'm Learning About TCP
I'm reading the preface to "Designing Data-Intensive Applications" and it says it assumes I know about TCP, which I really don't.

# Resources
- as ever, [Real Python](https://realpython.com/python-sockets/#background)

# How To Explore 
- run `python echo_server.py`
- run `netstat -an -ptcp | grep LISTEN` and look for the matching entry
- run `lsof -i -n` and look for the matching entry 
- run `python echo_client.py` in another window
