# pip install pymongo
from pymongo import MongoClient

# Client 연결(서버)
# client = MongoClient('localhost', 27017)
client = MongoClient('mongodb://localhost:27017/')

# Database 연결
# db = client.test
db = client['test']

# collection 연결
# collection = db.score
collection = db['score']

result = collection.find()
# print(result)
for res in result:
    print(res)
