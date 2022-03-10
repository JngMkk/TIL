from pymongo import MongoClient

cli = MongoClient('localhost', 27017)
db = cli.test
score = db.score

result = score.insert_many(
    [
        {"name" : "한지민", "kor" : 100, "eng" : 30, "math" : 50},
        {"name" : "송강", "kor" : 50, "eng" : 100, "math" : 70},
    ]
)

print(result)
print(result.inserted_ids)

result = score.insert_one(
    {"name" : "신민아", "kor" : 50, "eng" : 70, "math" : 100}
)

print(result)
print(result.inserted_id)