# Projeto de Transferência de Arquivos

Este projeto permite que você compartilhe arquivos de forma simples e eficiente. Ele consiste em dois programas Python que facilitam a transferência de arquivos entre você e seus colegas.

### localhost.py - Servidor HTTP
O script Python localhost.py é responsável por criar um servidor HTTP  para "hospedar" um arquivo de sua escolha. Após configurar as regras do firewall utilizando os bats, siga estas etapas para usar o servidor:

Execute o arquivo localhost.py.
Ele solicitará que você insira o nome do arquivo e sua extensão.
O arquivo deve estar no mesmo diretório que o localhost.py.
O servidor estará disponível em http://seu_ip:8080/, servindo o arquivo especificado.


### url.py - Cliente de Download
O script Python url.py permite que um colega baixe o arquivo do servidor criado com o localhost.py. Para usá-lo, siga estas etapas:

Execute o arquivo url.py.
Ele solicitará a URL do servidor (por exemplo, http://seu_endereco_ip:8080/).
Ele solicitará o nome do arquivo com a extensão.
O cliente fará o download do arquivo do servidor e o salvará localmente.
Certifique-se de compartilhar a URL do servidor (gerada automaticamente pelo servidor HTTP) com o seu colega para que eles possam baixar o arquivo.
## Configuração (Windows)

Antes de executar os programas Python, é necessário configurar as regras do firewall no Windows para permitir o tráfego na porta 8080. Você pode fazer isso executando os seguintes .bats:

### Permitir Tráfego na Porta 8080

Execute o seguinte script para permitir o tráfego na porta 8080:

```batch
@echo off
echo Permitindo tráfego para a porta 8080
netsh advfirewall firewall add rule name="Permit Porta 8080" dir=in action=allow protocol=TCP localport=8080
echo Regra Criada.
pause
```
### Excluir Regra de Tráfego
Se você desejar excluir a regra que permite o tráfego na porta 8080, execute o seguinte script:

```batch
Copy code
@echo off
echo Excluindo regra que permite o tráfego
netsh advfirewall firewall delete rule name="Permit Porta 8080"
echo Regra excluída.
pause
```

### Requisitos
Linguagem de Programação: Python
Bibliotecas: http.server, urllib, alive-progress
```batch
 pip install alive-progress
```

<img align="center" alt="Python Logo" height="50" width="50" src="https://github.com/devicons/devicon/blob/master/icons/python/python-original.svg">

