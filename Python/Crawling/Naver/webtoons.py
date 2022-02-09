# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup as bs
import requests
import json

url = "https://comic.naver.com/webtoon/weekdayList?week=wed"
# html = requests.get(url) : response([200])
html = requests.get(url).text
soup = bs(html, 'html.parser')

# 방법 1
toons = soup.select("ul.img_list > li > dl")
titles = []
ratings = []
for toon in toons:
    title = toon.find('a')['title']
    rating = toon.find('strong').text
    titles.append(title)
    ratings.append(rating)

json_datas = [{'titles': t, 'rating': r} for t, r in zip(titles, ratings)]
web_dic = dict()
web_dic['webtoons'] = json_datas
json_data = json.dumps(web_dic, ensure_ascii=False)
# print(web_dic)
# print(json_datas)
# print(json.dumps(json_datas, ensure_ascii=False))

# 방법 2
webtoons = soup.find('ul', {'class': 'img_list'}) 
dl_list = webtoons.select('dl')
lst = []
for dl in dl_list:
    title = dl.find('a')['title']
    rating = dl.find('strong').text
    tmp = dict()
    tmp['title'] = title
    tmp['rating'] = rating
    lst.append(tmp)
# print(lst)
res = dict()
res['webtoons'] = lst
# print(res)
res_json = json.dumps(res, ensure_ascii=False)
# print(res_json)
with open('./webtoons.json', 'w') as f:
    f.write(res_json)

# encoding
# with open('./webtoons.json', 'w', encoding='utf-8') as f:
#   f.write(res_json)