# Instagram Crawling
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import re
import time
import unicodedata

service = webdriver.chrome.service.Service('/usr/local/bin/chromedriver')
driver = webdriver.Chrome(service=service)


# 인스타그램 접속하기
driver.get('https://www.instagram.com')
time.sleep(3)

# 인스타그램 로그인하기
email = input("email : ")
input_id = driver.find_elements_by_css_selector('input._2hvTZ.pexuQ.zyHYP')[0]
input_id.clear()
input_id.send_keys(email)

password = input("password : ")
input_pw = driver.find_elements_by_css_selector('input._2hvTZ.pexuQ.zyHYP')[1]
input_pw.clear()
input_pw.send_keys(password)
input_pw.submit()
time.sleep(5)

# 검색결과 URL 만들기 with 함수
def insta_searching(word):
    url = 'https://www.instagram.com/explore/tags/' + word
    return url

# HTML에서 첫번째 게시글 찾아 클릭하기
def select_first(driver):
    first = driver.find_element_by_css_selector("div._9AhH0")
    first.click()
    time.sleep(5)

# 게시글 정보 가져오기
def get_content(driver):
    # 1. 현재 페이지 html 정보 가져오기
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    # 2. 본문 내용 가져오기
    try :
        content = soup.select('div.C4VMK > span')[0].text
        content = unicodedata.normalize('NFC', content)
    except :
        content = ' '
    # 3. 본문 내용에서 해시태그를 가져오기(정규식 활용)
    tags = re.findall(r'#[^\s#,\\]+', content)
    # 4. 작성일자 정보 가져오기
    date = soup.select('time._1o9PC.Nzb55')[0]['datetime'][:10]
    # 5. 종아요 수 가져오기
    try :
        like = soup.select('div.Nm9Fw')[0].text.split(' ')[1].split('개')[0]
    except :
        like = 0
    # 6. 위치정보 가져오기
    try :
        place = soup.select('div.M30cS')[0].text
        place = unicodedata.normalize('NFC', place)
    except :
        place = ''
    # 7. 수집한 정보 저장하기
    data = [content, date, like, place, tags]
    return data

# 다음 게시글 열기
def move_next(driver) :
    right = driver.find_element(By.CSS_SELECTOR, 'div._l8mY4_feth3 > button')
    right.click()
    time.sleep(3)

# 인스타그램 크롤링
word = '잠실카페'
url = insta_searching(word)

driver.get(url)
time.sleep(10)

first = driver.find_element_by_css_selector("div._9AhH0")
first.click()
time.sleep(3)

# 비어있는 변수(results)만들기
results = [ ]

# 여러 게시글 수집하기
target = 500 # 크롤링할 게시글 수
for i in range(target) :
    # 게시글 수집에 오류 발생 시 2초 대기 후, 다음 글로 넘어가게 하기
    try :
        data = get_content(driver)
        results.append(data)
        move_next(driver)
    except :
        time.sleep(10)
        move_next(driver)

print(results[:2])

# 크롤링 결과 저장하기

import pandas as pd
results_df = pd.DataFrame(results)
results_df.columns = ['content', 'data', 'like', 'place', 'tags']
results_df.to_excel(f'./files/1_crawling_{word}_500.xlsx')