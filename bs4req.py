


import requests as r 
from bs4 import BeautifulSoup

html = r.get('https://pymug.com').text

soup = BeautifulSoup(html, 'html.parser')

print(soup.text)