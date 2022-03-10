"""
1. starbucks_all.json 읽어옴
2. 읽어온 파일 한 줄씩 json_data로 저장
3. json_data를 dictionary로 변환 (result_dict)
    result_dict에 "list"라는 키를 입력하여, 리턴된 value를 반복문으로 출력
4. mongodb와 연결 (db : test / collection : starbucks01)
5. result_dict['list'] 값을 mongodb에 저장
6. starbucks01 collection 전체 출력
"""
import json
from pymongo import MongoClient

with open("starbucks_all.json", "r") as f:
    json_data = f.readline()

result_dict = json.loads(json_data)

# for data in result_dict['list']:
#     print(data)

cli = MongoClient("localhost", 27017)
db = cli.test
starbucks01 = db.starbucks01

res = starbucks01.insert_many(result_dict['list'])
print(res)

all = starbucks01.find({})
for data in all:
    print(data)