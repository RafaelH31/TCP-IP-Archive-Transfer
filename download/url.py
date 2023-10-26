from urllib import request
from alive_progress import alive_bar
import time

#oi
def a():
    for total in 5000, 7000, 4000, 0:
        with alive_bar(total) as bar:
            for _ in range(5000):
                time.sleep(.001)
                bar()

print("insira url do quer baixar")
url = input()

print("insira o nome e a extensão do arquivo")
file = input()

request.urlretrieve(url, file)
value = True 
while (value):
    a()

