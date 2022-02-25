"""
Adapted from https://realpython.com/python-sockets/#background

Changes I've made in adapting:
    - remove optional arguments to `socket.socket()` since they were == default
    - rename the two socket instances to something more descriptive
    - type hinted the values returned by `socket.accept()`
"""
from socket import socket

HOST = '127.0.0.1'
PORT = 65432

with socket() as listening_socket:
    listening_socket.bind((HOST, PORT))
    listening_socket.listen()

    communicating_socket: socket
    addr: tuple[str, int]
    communicating_socket, addr = listening_socket.accept()

    remote_host, remote_port = addr
    assert remote_host == HOST
    assert remote_port != PORT # the port is assigned from a random set of ports

    with communicating_socket:
        print(f"Connected to addr: {addr}")
        while True:
            incoming_data = communicating_socket.recv(1024)
            if not incoming_data:
                break
            communicating_socket.sendall(incoming_data)
