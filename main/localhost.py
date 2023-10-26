from http.server import HTTPServer, BaseHTTPRequestHandler
print("insira o nome do arquivo e a extensão dele ")
a = input()

class Servidor(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == '/':
            self.path = '/{}'.format(a)
        try:
            if self.path.endswith('.html'):
                content_type = 'text/html'
            elif self.path.endswith('.jpg'):
                content_type = 'image/jpeg'
                #aqui vai ficar grande
            else:
                #basicamente código
                content_type = 'text/plain'
            file_to_open = open(self.path[1:], 'rb').read()
            self.send_response(200)
        except FileNotFoundError:
            file_to_open = "O arquivo não foi encontrado"
            self.send_response(404)
        self.send_header('Content-type', content_type)
        self.end_headers()
        self.wfile.write(file_to_open)

httpd = HTTPServer(('0.0.0.0', 8080), Servidor)

httpd.serve_forever()
