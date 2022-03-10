from pymongo import MongoClient
from pprint import pprint

client = MongoClient('localhost', 27017)
db = client.test

# cursor = db.score.find()
# print(cursor)

score = db.score
cursor = score.find()
for doc in cursor:
    print(doc)
    # pprint(doc)

lee = score.find({"name" : "이순신"})
for doc in lee:
    # pprint(doc)
    pass

lee2 = score.find_one({"name" : "이순신"})
# pprint(lee2)

# print("score collection 안에 있는 doc 총 개수 :", score.count_documents({}))

# 국어 점수가 60점보다 큰 doc 전체 출력
tmp = score.find({"kor" : {"$gt" : 60}}, {"_id": 0})
for doc in tmp:
    # print(doc)
    pass