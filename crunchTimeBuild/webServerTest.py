import http.server
import socketserver

# Web Server Portion #################

webPORT = 80
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", webPORT), Handler) as httpd:
    print("web serving at port", webPORT)
    httpd.serve_forever()

