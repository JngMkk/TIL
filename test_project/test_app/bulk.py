import json
from elasticsearch import Elasticsearch

es = Elasticsearch([{'host':'localhost','port':'9200'}])

es.indices.create(
    index="dictionary",
    body={
        "settings": {
            "index": {
                "analysis": {
                    "analyzer": {
                        "my_analyzer": {
                            "type": "custom",
                            "tokenizer": "nori_tokenizer"
                        },
                        "english" : {
                            "type": "custom",
                            "tokenizer": "standard",
                            "filter" : [
                                "lowercase"
                            ]
                        }
                    }
                }
            }
        },
        "mappings": {
            "properties": {
                "name": {
                    "type": "text",
                    "analyzer": "my_analyzer"
                },
                "botanyNm": {
                    "type": "text",
                    "analyzer": "english"
                },
                "info": {
                    "type": "keyword"
                },
                "waterCycle": {
                    "type": "keyword"
                },
                "waterInfo": {
                    "type": "keyword"
                },
                "waterExp": {
                    "type": "keyword"
                },
                "waterExpInfo": {
                    "type": "keyword"
                },
                "light": {
                    "type": "keyword"
                },
                "lightInfo": {
                    "type": "keyword"
                },
                "lightExp": {
                    "type": "keyword"
                },
                "lightExpInfo": {
                    "type": "keyword"
                },
                "humidity": {
                    "type": "keyword"
                },
                "humidInfo": {
                    "type": "keyword"
                },
                "humidExp": {
                    "type": "keyword"
                },
                "humidExpInfo": {
                    "type": "keyword"
                },
                "tempExp": {
                    "type": "keyword"
                },
                "tempExpInfo": {
                    "type": "keyword"
                }
            }
        }
    }
)

directory_path = "/home/jngmk/workspace/go/src/github.com/JngMkk/data/"
with open(directory_path + "fuleaf.json", encoding="utf-8") as file:
    json_data = json.loads(file.read())

body = ""
count = 1
for i in json_data:
    body = body + json.dumps({"index": {"_index": "dictionary", "_id": count}}) + "\n"
    body = body + json.dumps(i, ensure_ascii=False) + "\n"
    if count == 1:
        print(body)
    count += 1

f = open("./input.json", "w")
f.write(body)
f.close()

es.bulk(body)