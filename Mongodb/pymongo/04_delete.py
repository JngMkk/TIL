from pymongo import MongoClient

cli = MongoClient("localhost", 27017)
db = cli.test
score = db.score

result = score.delete_one(
    {"name" : "유재석"}
)

print(result)
print(result.deleted_count)

# test field가 없는 doc들 모두 삭제
result = score.delete_many(
    {"test" : {"$exists" : False}}
)

print(result.deleted_count)