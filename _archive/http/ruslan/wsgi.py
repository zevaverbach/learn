import datetime as dt
import io
import socket
import sys


class WSGIServer:

    def __init__(self, server_address):
        listen_socket = socket.socket()
        listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        listen_socket.bind(server_address)
        listen_socket.listen()
        host, port = listen_socket.getsockname()[:2]
        self.server_name = socket.getfqdn(host)
        self.server_port = port
        self.headers_set = []
        self.listen_socket = listen_socket
        self._application = None

    def set_app(self, application):
        self._application = application

    def serve_forever(self):
        while True:
            self.client_connection, _ = self.listen_socket.accept()
            self.handle_one_request()

    def handle_one_request(self):
        request_data = self.client_connection.recv(1024).decode('utf-8')
        try:
            method, path, version = request_data.splitlines()[0].rstrip('\r\n').split()
        except IndexError:
            result = [b'']
        else:
            env = {
                    # WSGI vars
                    'wsgi.version': (1, 0),
                    'wsgi.url_scheme': 'http',
                    'wsgi.input': io.StringIO(request_data),
                    'wsgi.errors': sys.stderr,
                    'wsgi.multithread': False,
                    'wsgi.multiprocess': False,
                    'wsgi.run_once': False,
                    # CGI vars
                    'REQUEST_METHOD': method,
                    'PATH_INFO': path,
                    'SERVER_NAME': self.server_name,
                    'SERVER_PORT': str(self.server_port),
            }
            result = self._application(env, self.start_response)
        self.finish_response(result)

    def start_response(self, status, response_headers, exc_info=None):
        """
        This is called by the _application.
        """
        server_headers = [
            ('Date', str(dt.datetime.now())),
            ('Server', 'WSGIServer 0.2'),
        ]
        self.headers_set = [status, response_headers + server_headers]
    
    def finish_response(self, result):
        try:
            status, response_headers = self.headers_set
            response = (
                f'HTTP/1.1 {status}\r\n'
                + '\r\n'.join([f'{key}: {val}' for key, val in response_headers])
                + '\r\n\r\n'
                + ''.join([data.decode('utf-8') for data in result])
            ).encode()
            self.client_connection.sendall(response)
        finally:
            self.client_connection.close()


def make_server(application, server_address: tuple[str, int] | None = None):
    server = WSGIServer(server_address)
    server.set_app(application)
    return server


if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit('Provide a WSGI application object as module:callable')
    app_path = sys.argv[1]
    if ":" not in app_path:
        sys.exit("Provide a module:app")
    module, application = app_path.split(':')
    module = __import__(module)
    application = getattr(module, application)
    httpd = make_server(application, ('', 8888))
    httpd.serve_forever()
