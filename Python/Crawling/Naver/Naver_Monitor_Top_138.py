import time
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

def scroll() :
    last_page_height = driver.execute_script("return document.documentElement.scrollHeight")
    for i in range(5):
        driver.execute_script('window.scrollTo(0, document.documentElement.scrollHeight)')
        time.sleep(3)
        new_page_height = driver.execute_script("return document.documentElement.scrollHeight")
    
        if new_page_height == last_page_height:
            break
        last_page_height = new_page_height

driver = webdriver.Chrome(r'C:\Users\JngMK\Desktop\2021KNUpython2/chromedriver')
url = 'https://search.shopping.naver.com/search/all?query=%EB%AA%A8%EB%8B%88%ED%84%B0&cat_id=&frm=NVSHATC'
driver.get(url)
time.sleep(3)

title = []
ad = []
lowest_price = []
review_count = []
at = []
href = []
btn = driver.find_element_by_css_selector('#__next > div > div.style_container__1YjHN > div > div.style_content_wrap__1PzEo > div.style_content__2T20F > div.pagination_pagination__6AcG4 > a.pagination_next__1ITTf')

for i in range(3):
    scroll()
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    goods = soup.select('div.basicList_info_area__17Xyo')
    for good in goods :
        try :
            title.append(good.select_one('a.basicList_link__1MaTN').text)
            lowest_price.append(good.select_one('span.price_num__2WUXn').text.split('원')[0])
            at.append(good.select_one('div.basicList_etc_box__1Jzg6').text.strip().split('찜')[0].split('일')[1])
            href.append(good.select_one('a.basicList_link__1MaTN')['href'])
            if good.select_one('div.basicList_price_area__1UXXR> button').text == '광고' :
                ad.append(1)
        except AttributeError :
            ad.append(0)
    for good in goods :
        try :
            review_count.append(good.select_one('em.basicList_num__1yXM9').text)
        except AttributeError :
            review_count.append(0)
    btn.click()
    time.sleep(10)

naver_monitor_df = pd.DataFrame([title, lowest_price, review_count, at, href, ad]).T
naver_monitor_df.columns = ['물품', '최저 가격', '리뷰 수', '등록일', 'href', '광고 유무']
naver_monitor_df.to_excel('../naver_file/naver_shopping_monitor_top138_{}.xlsx'.format(datetime.today().strftime("%Y%m%d")))