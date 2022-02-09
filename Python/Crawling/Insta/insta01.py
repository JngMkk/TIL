# import requests
# from bs4 import BeautifulSoup as bs

# tag = input('search tags: ')
# url = f'https://www.instagram.com/explore/tags/{tag}'
# html = requests.get(url).text
# soup = bs(html, 'html.parser')      # 못불러온다..

from bs4 import BeautifulSoup as bs
from selenium import webdriver
import re
import time
import unicodedata

service = webdriver.chrome.service.Service('/usr/local/bin/chromedriver')
driver = webdriver.Chrome(service=service)

# 검색결과 URL 만들기 with 함수

def insta_searching(word):
    
    url = 'https://www.instagram.com/explore/tags/' + word
    return url

# 검색결과 페이지 접속하기

tag = input('search tags: ')
url = insta_searching(tag)
driver.get(url)
# driver.implicitly_wait(3)
time.sleep(3)

soup = bs(driver.page_source, 'html.parser')
img_list = soup.find_all('div', class_='KL4Bh')

for img in img_list:
    print(img)