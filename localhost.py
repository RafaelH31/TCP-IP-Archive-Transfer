from http.server import HTTPServer, BaseHTTPRequestHandler

class Servidor(BaseHTTPRequestHandler):

    def do_GET(self):
       if self.path == '/':
           self.path = '/test.html'
       try:
           file_to_open = open(self.path[1:]).read()
           self.send_response(200)
       except:
           file_to_open = "O aqrquivo não foi achado"
           self.send_response(404)
       self.end_headers()
       self.wfile.write(bytes(file_to_open, 'utf-8'))

httpd = HTTPServer(('localhost',8080),Servidor)
httpd.serve_forever()
