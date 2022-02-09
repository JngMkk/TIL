from bs4 import BeautifulSoup as bs
import urllib.request
import pandas as pd

html = urllib.request.urlopen("https://movie.naver.com/movie/running/current.naver#")
soup = bs(html, 'html.parser')

# 방법 1
movies = soup.select("dt.tit > a")
ratings = soup.select("a > span.num")
titles = []
rating = []
for data in movies:
    titles.append(data.text)
for rate in ratings:
    rating.append(rate.text)
df = pd.DataFrame([titles, rating]).T
df.columns = ['제목', '평점']

# 방법 2
movies = soup.find_all('dl', class_='lst_dsc')
for movie in movies:
    # 제목
    title = movie.find('a').text
    # 벌점
    rating = movie.find('span', class_='num').text
    # print(f'{title} [{rating}]')