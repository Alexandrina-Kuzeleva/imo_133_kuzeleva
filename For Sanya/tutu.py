import requests
from bs4 import BeautifulSoup as BS 

url = 'https://api-x.tutu.ru/v2/data'
r = requests.get(url)
soup = BS(r.content, 'html.parser')
print(soup)
