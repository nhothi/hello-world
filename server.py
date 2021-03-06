from http.server import HTTPStatus, BaseHTTPRequestHandler
from socketserver import TCPServer

PORT = 8000
MESSAGE = "Hello, world!\ni am alive and well\n".encode("ascii")


class Handler(BaseHTTPRequestHandler):
    """Respond to requests with hello."""

    def do_GET(self):
        """Handle GET"""
        self.send_response(HTTPStatus.OK)
        self.send_header("Content-type", "text/plain")
        self.send_header("Content-length", len(MESSAGE))
        self.end_headers()
        self.wfile.write(MESSAGE)


print("Serving at port", PORT)
TCPServer.allow_reuse_address = True
httpd = TCPServer(("", PORT), Handler)
httpd.serve_forever()
