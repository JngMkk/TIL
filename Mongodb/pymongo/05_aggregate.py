from pymongo import MongoClient

cli = MongoClient("localhost", 27017)
db = cli.test
score = db.score

aggr = score.aggregate(
    [
        {"$match":
            {"kor" : {"$gt" : 50}}},
        {"$group":
            {"_id" : "kor", "sum" : {"$sum" : "$kor"}}}
    ]
)

print(aggr)
print(list(aggr))