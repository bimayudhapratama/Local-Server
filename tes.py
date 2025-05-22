from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse

class ChatHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urllib.parse.urlparse(self.path)
        query = urllib.parse.parse_qs(parsed_path.query)
        message = query.get("msg", [""])[0]
        
        # Baca template HTML
        with open("chat.html", "r", encoding="utf-8") as f:
            html = f.read().replace("{{MESSAGE}}", message)

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(html.encode())

if __name__ == "__main__":
    server_address = ("", 8080)
    httpd = HTTPServer(server_address, ChatHandler)
    print("Server berjalan di http://<IP-laptop>:8000?msg=Pesan")
    httpd.serve_forever()
