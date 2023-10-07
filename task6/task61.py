
import requests
from bs4 import BeautifulSoup as BS
url = 'https://habr.com/ru/articles/top/weekly/'
r = requests.get(url)
soup = BS(r.content, 'html.parser')
links = soup.find_all('a', class_='tm-title__link')
'''print(links)
for l in links:
    print('https://habr.com'+ l.get('href'))
    print(str(l.get('href'))[-7:-1])
    r_art = requests.get('https://habr.com'+ l.get('href'))
    soup = BS(r_art.content, 'html.parser')'''

for l in links:
    link = 'https://habr.com'+ l.get('href')
    link_num = str(l.get('href'))[-7:-1]
    r_art = requests.get(link)
    soup = BS(r_art.content, 'html.parser')
    with open(link_num + '.html', 'w', encoding='utf-8') as file:
        file.write(str(soup))



