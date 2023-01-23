# Purpose
I started learning `tcp` from [a Real Python post][1] in the sister directory of this repo called `tcp`. It started going into concurrency and `select()` and I got a bit lost. I'll try to circle back to it, but since the only way I'll actually be using TCP (I imagine) is via HTTP, I thought I'd jump over and learn how a web server works.

As it turns out, the resources I found for building a web server from scratch in Python cover `tcp` in a very similar way to [the Real Python post][1].

# Resources (found via Full Stack Python)
1) [uses `socket`](https://joaoventura.net/blog/2017/python-webserver/)
1) [uses `socket` too](https://ruslanspivak.com/lsbaws-part1/)
1) [uses BaseHTTPServer](http://aosabook.org/en/500L/a-simple-web-server.html) from the stdlib

[1]: https://realpython.com/python-sockets/#background

# Exercises
- [ ] implement a WSGI web server in <= 100 lines of Python (see `ruslan/wsgi.py`) 
- [ ] implement a WSGI-compliant web framework in X lines of Python (see Ruslan post)
