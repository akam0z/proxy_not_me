import http.server
import socketserver
import urllib.request

PORT = 8080

class Proxy(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith("http://"):
            url = self.path[7:]
            req = urllib.request.Request(url)
            with urllib.request.urlopen(req) as response:
                self.send_response(response.status)
                self.send_header("Content-type", response.headers.get_content_type())
                self.end_headers()
                self.wfile.write(response.read())
        else:
            super().do_GET()

handler = Proxy
with socketserver.TCPServer(("", PORT), handler) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()
