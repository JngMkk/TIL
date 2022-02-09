from bs4 import BeautifulSoup as bs
import requests

# url="https://www.data.go.kr/tcs/dss/selectDataSetList.do?dType=FILE&keyword=%EA%B5%90%EC%9C%A1&currentPage=5"
# html = requests.get(url).text
# soup = bs(html, 'html.parser')

# lst = soup.select('div.result-list > ul > li')
# titles = []
# for elem in lst:
#     title = elem.find('span', class_='title').text.strip()
#     titles.append(title)
# print(titles)

# titles = soup.find_all('span', class_='title')
# for title in titles:
#     print(title.text.strip())

# # 방법 1
# page_nav = soup.find('nav', class_="pagination")
# nums = []
# for num in page_nav:
#     if num.has_attr('class'):
#         if num['class'] == ['active']:
#             nums.append(int(num.text))
#         else:
#             continue
#     else:
#         nums.append(int(num.text))
# titles = []
# for i in nums:
#     url = f"https://www.data.go.kr/tcs/dss/selectDataSetList.do?dType=FILE&keyword=%EA%B5%90%EC%9C%A1&currentPage={i}"
#     soup = bs(requests.get(url).text, 'html.parser')
#     title = soup.find_all('span', class_='title')
#     for t in title:
#         titles.append(t.text.strip())
# print(titles)

# 방법 2
# page_nav = soup.find('nav', class_="pagination")
# nums = []
# for page in page_nav:
#     if page.text.isdigit():
#         nums.append(page.text)
# print(nums)


url="https://www.data.go.kr/tcs/dss/selectDataSetList.do?dType=FILE&keyword=%EA%B5%90%EC%9C%A1&currentPage=5"
html = requests.get(url).text
soup = bs(html, 'html.parser')

page_nav = soup.find('nav', class_="pagination")
nums = list(filter(None, map(lambda x: x.text if x.text.isdigit() else None, page_nav)))

url="https://www.data.go.kr/tcs/dss/selectDataSetList.do?dType=FILE&keyword=%EA%B5%90%EC%9C%A1&currentPage="

for i in nums:
    soup = bs(requests.get(url+i).text, 'html.parser')
    titles = soup.select('span[class=title]')
    for title in titles:
        print(title.text.strip())