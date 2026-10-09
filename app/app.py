from http.server import BaseHTTPRequestHandler, HTTPServer
import os


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/health":
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"healthy")
        else:
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(
                b"Hello from the DevOps Starter Kit!"
            )


server = HTTPServer(
    ("0.0.0.0", int(os.getenv("PORT", "8080"))),
    Handler,
)
server.serve_forever()

