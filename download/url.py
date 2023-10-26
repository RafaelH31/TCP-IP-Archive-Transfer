from urllib import request
from alive_progress import alive_bar
import time

def download(url, file):
    request.urlretrieve(url, file)
    with alive_bar(20, title="Download em andamento") as bars:
        for _ in range(10):
            time.sleep(1)  
            bars()

url = input("Insira a URL que deseja baixar: ")
file = input("Insira o nome e a extensão do arquivo: ")

download(url, file)
print(f"Download de {file} concluído com sucesso!")
