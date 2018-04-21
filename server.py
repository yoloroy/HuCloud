from http.server import BaseHTTPRequestHandler, HTTPServer
import requests


class HttpProcessor(BaseHTTPRequestHandler):
    def do_GET(self):
        body = self.rfile.read().decode('utf-8')
        print(body)

        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()
        self.wfile.write('Не110!'.encode())

    def do_POST(self):
        body = self.rfile.read().decode('utf-8')
        print(body)

        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()
        self.wfile.write('Не110!'.encode())

if __name__ == '__main__':
    serv = HTTPServer(("192.168.0.194", 80), HttpProcessor)
    serv.serve_forever()
