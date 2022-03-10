from pymongo import MongoClient

cli = MongoClient("mongodb://localhost:27017")
db = cli["test"]
score = db["score"]

# 이름이 유재석인 doc 찾아서 midterm의 kor 점수를 100점으로 변경하자
result = score.update_one(
    {"name" : "유재석"},
    {"$set" : {"midterm.kor" : 100}}
)

print(result.matched_count)
print(result.modified_count)

result = score.update_many(
    {"eng" : {"$gt" : 80}},
    {"$set" : {"eng" : 0}}
)

print(result.matched_count)
print(result.modified_count)