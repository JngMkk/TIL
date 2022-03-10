import json
from pymongo import MongoClient

with open("starbucks_all.json", "r") as f:
    json_data = f.readline()

result_dict = json.loads(json_data)

geo_list = []
for data in result_dict["list"]:
    geo_dict = {}
    geo_dict["s_name"] = data["s_name"]
    coordinates = [float(data["lot"]), float(data["lat"])]
    geo_dict["location"] = {"type" : "Point", "coordinates" : coordinates}
    geo_list.append(geo_dict)

# print(geo_list)

cli = MongoClient("localhost", 27017)
db = cli.test
starbucks02 = db.starbucks02

res = starbucks02.insert_many(geo_list)
print(len(res.inserted_ids))

# ------------------------------------------------------------------------
# Mongodb shell에서 작업
# db.starbucks02.createIndex({location:"2dsphere"})
# 내 위치 : 37.5248171381127, 127.05505428317193

# 내 위치 기준 주변 검색
# db.starbucks02.find(
#     {
#         location: {
#             $near: {
#                 $geometry:{
#                     type: "Point",
#                     coordinates: [127.05505428317193, 37.5248171381127]
#                 },
#                 $maxDistance: 500
#             }
#         }
#     }
# )

# 현재 위치부터 ~ "서울" 단어가 포함된 좌표들의 거리
# db.starbucks02.aggregate(
#     [
#         {
#             $geoNear:{
#                 near:{
#                     type: "Point",
#                     coordinates : [127.05505428317193, 37.5248171381127]
#                 },
#                 spherical : true,
#                 query: {s_name: /서울/},
#                 distanceField: "distance"
#             }
#         }
#     ]
# )

# 평면 내 검색
# 강남 : 127.02761159460194, 37.49803675628153
# 선정릉 : 127.04391325768417, 37.510487444168355
# 학여울 : 127.07050608281472, 37.496836198102905
# db.starbucks02.find(
#     {
#         location:{
#             $geoIntersects: {
#                 $geometry: {
#                     type: "Polygon",
#                     coordinates: [
#                                     [
#                                         [127.02761159460194, 37.49803675628153],
#                                         [127.04391325768417, 37.510487444168355],
#                                         [127.07050608281472, 37.496836198102905],
#                                         [127.02761159460194, 37.49803675628153]
#                                     ]
#                     ]
#                 }
#             }
#         }
#     }
# )

# 원
# db.starbucks02.find(
#     {
#         location: {
#             $geoWithin: {
#                 $centerSphere: [[127.05505428317193, 37.5248171381127], 0.5/3963.2]
#             }
#         }
#     }
# )
# ------------------------------------------------------------------------