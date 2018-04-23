from http.server import BaseHTTPRequestHandler, HTTPServer
import requests


class HttpProcessor(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path=='/':
            self.send_response(200)
            self.send_header('content-type', 'text/html')
            self.end_headers()
        body= ['<html><head><meta charset = "utf-8"> <title>Отправка файла</title></head>',
            '<body><form',
            'enctype = "multipart/form-data"',
            'method = "post"',
            'action = "http://192.168.0.194/postfile/">',
            '<p><input type = "file" name = "file"/></p>',
            '<p><p><input type = "submit" value = "Отправить" /> </p> </form> </body> </html>'
            ]
        for i in body:
            self.wfile.write (i.encode())
            self.wfile.write ('\n'.encode())
#body = self.rfile.read().decode('utf-8')
        #print(body)

    def do_POST(self):
        print(self.path)
        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()
        if self.path == '/postfile/':
            self.wfile.write('Received!'.encode())
            print (self.path)

if __name__ == '__main__':
    serv = HTTPServer(("192.168.0.194", 80), HttpProcessor)
    serv.serve_forever()
