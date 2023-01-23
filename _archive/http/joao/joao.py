from pathlib import Path
import socket

from rich import print

HOST, PORT = '', 8888

socket_connection = socket.socket()
socket_connection.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
socket_connection.bind((HOST, PORT))
socket_connection.listen(1)
print(f'Serving HTTP on port {PORT} ...')

while True:
    client_connection, client_address = socket_connection.accept()
    request_data = client_connection.recv(1024)
    request, *headers = [h.strip() for h in request_data.decode('utf-8').split('\n') if h.strip()]
    header_dict = {h.split(':')[0]: h.split(':')[1].strip() for h in headers}
    method, filename, http_version = request.split()

    print("filename:", filename)

    str_or_bytes = "str"
    if filename == "/favicon.ico":
        filename = "favicon-16x16.png"
        str_or_bytes = "bytes"
    elif filename == "/":
        filename = "index.html"

    try:
        if str_or_bytes == "bytes":
            the_bytes = Path(filename).read_bytes()
        else:
            the_bytes = Path(filename).read_text().encode()
        http_response = b"HTTP/1.1 200 OK\n\n" + the_bytes
    except FileNotFoundError:
        http_response = b'HTTP/1.0 404 NOT FOUND\n\nFile Not Found'

    client_connection.sendall(http_response)
    client_connection.close()
