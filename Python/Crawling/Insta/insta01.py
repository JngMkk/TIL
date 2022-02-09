import requests
from bs4 import BeautifulSoup as bs

url = "https://www.instagram.com/explore/tags/python/"
html = requests.get(url).text
soup = bs(html, 'html.parser')
path = soup.find('div', class_='KL4Bh')