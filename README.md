# Projeto de Transferência de Arquivos

Este projeto permite que você abra uma porta para servir um arquivo de sua escolha, enquanto um colega pode se conectar a essa porta e baixar o arquivo. O projeto consiste em dois programas Python.

## `localhost.py` - Abre servidor HTTP

É responsável por criar um servidor HTTP local para "hostear" um arquivo escolhido. 

### Como usar o servidor:

1. Execute o arquivo `localhost.py`.
2. Ele solicitará que você insira o nome do arquivo e sua extensão.
3. O arquivo deve estar no mesmo diretório que o `localhost.py`
5. O servidor estará disponível em `http://localhost:8080/`, servindo o arquivo especificado.

## `url.py` - Faz Download pelo link

O segundo código permite que um colega baixe o arquivo do servidor criado com o `localhost.py`.

### Como usar o cliente de download:

1. Execute o arquivo `url.py`.
2. Ele solicitará a URL do servidor (ex: `http://seu_endereco_ip:8080/`)
3. Ele solicitará o nome do arquivo com a extensão.
4. O cliente fará o download do arquivo do servidor e o salvará localmente.

Certifique-se de compartilhar a URL do servidor (gerada automaticamente pelo servidor HTTP) com o seu colega para que eles possam baixar o arquivo.

Divirta-se compartilhando arquivos com facilidade usando este projeto de transferência de arquivos!

## Requisitos
- Linguagem de Programação: Python
- Bibliotecas: http.server, urllib

<img align="center" alt="Python Logo" height="50" width="50" src="https://github.com/devicons/devicon/blob/master/icons/python/python-original.svg">
