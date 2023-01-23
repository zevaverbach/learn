# https://realpython.com/python-sockets/#background
import socket

HOST = '127.0.0.1'
PORT = 65432

with socket.socket() as client:
    client.connect((HOST, PORT))
    client.sendall(b"Hello, world!")
    response = client.recv(1024)

print(f"Received {response}")
