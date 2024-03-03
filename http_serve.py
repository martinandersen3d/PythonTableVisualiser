from http.server import BaseHTTPRequestHandler, HTTPServer
from html_render import render_html_table

class HTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        # Assuming data is passed from main.py
        if hasattr(self.server, 'data'):
            data = self.server.data
            html_content = render_html_table(data)
            self.wfile.write(html_content.encode())
        else:
            self.wfile.write(b"No data available")

def serve_http(host, port, data):
    server_address = (host, port)
    httpd = HTTPServer(server_address, HTTPRequestHandler)
    httpd.data = data  # Passing data to the server instance
    print(f"Server running on {host}:{port}")
    httpd.serve_forever()
