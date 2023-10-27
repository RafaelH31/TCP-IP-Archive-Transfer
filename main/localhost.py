from http.server import HTTPServer, BaseHTTPRequestHandler
import subprocess
import sys
import os

print("Insira o nome do arquivo e a extensão dele (por exemplo, arquivo.zip):")
a = input()

class Servidor(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/{}'.format(a)

        if self.path.endswith('.html'):
            content_type = 'text/html'
        elif self.path.endswith('.jpg'):
            content_type = 'image/jpeg'
        elif self.path.endswith('.zip'):
            content_type = 'application/zip'
        elif self.path.endswith('.txt'):
            content_type = 'text/plain'
        else:
            content_type = 'text/plain' # se não é nengum dos expecificados entra em plain text, salvando linhas de codigos e processo para as diversas liguagen e suas extensões que podems ser enviadas sendo que só são codigo emoji de oculos

        try:
            if not self.path.endswith('.zip'):
                file_to_open = open(self.path[1:], 'rb').read()
                self.send_response(200)
            else:
                with open(self.path[1:], 'rb') as binary_file:
                    file_to_open = binary_file.read()
                self.send_response(200)
        except FileNotFoundError:
            file_to_open = "O arquivo não foi encontrado"
            self.send_response(404)

        self.send_header('Content-type', content_type)
        self.end_headers()
        
        if not self.path.endswith('.zip'):
            self.wfile.write(file_to_open)
        else:
            self.send_header('Content-Disposition', f'attachment; filename="{os.path.basename(self.path)}"')
            self.wfile.write(file_to_open)

httpd = HTTPServer(('0.0.0.0', 8080), Servidor)
httpd.serve_forever()

print("Digite qualquer tecla para encerrar o programa e fechar a porta 8080")
opcao = input()
if opcao is not None:
    sys.exit()

    
