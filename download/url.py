from urllib import request

print("insira url do quer baixar")
url = input()

print("insira o nome e a extensão do arquivo")
file = input()

request.urlretrieve(url, file)
