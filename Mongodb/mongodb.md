# mongodb

## NoSQL

- 고정되지 않은 스키마
  - 필요할 때마다 필드를 추가 / 제거 -> 개발 속도 향상
- 데이터 간의 관계를 정의하지 않는 데이터베이스
  - db -> collection -> document
- 분산형 구조 (대용량 데이터 저장 용이)
  - sharding 지원 (클러스터 데이터 상호 복제)

## Shell

- Javascript interpreter 사용

  - js program, library, function 활용 가능

  ```
  > function test(){
  print('test')
  }
  
  > test()
  test
  
  > function test2(n){
  return n + 10;
  }
  
  > test2(3)
  13
  ```

## Structure

- database
  - 독립적인 하나의 권한
  - 각각의 database는 분리된 파일로 저장
- collection
  - document들의 group ( RDBMS - table )
  - schema를 가지지 않음 (document들의 field가 각각 다름)
- document
  - data record를 BSON(Binary JSON)으로 저장
  - field(key) 중복 불가

```
> show dbs
admin   0.000GB
config  0.000GB
local   0.000GB
test    0.000GB

> use test
switched to db test

> db
test

> db.jstest.insertOne(
	{
		name: 'test',
		age:100,
		class:'de'
	}
)

> db.jstest.insertOne(
	{
        name: 'mongo',
        class: 'db'
	}
)

> show collections
jstest

> db.jstest.find()
{ "_id" : ObjectId("622942fdaba64396557e6107"), "name" : "test", "age" : 100, "class" : "de" }
{ "_id" : ObjectId("62294319aba64396557e6108"), "name" : "mongo", "class" : "db" }
```

## CRUD

- db.collection.insert( document )

  ```
  > db.multi.insert(
  	{
  		name:'hong-gd', 
  		class:'de', 
  		midterm:
  			{kor: 100, eng: 60, math: 80}
  	}
  )
  WriteResult({ "nInserted" : 1 })
  ```

- db.collection.insertOne( document )

  ```
  > db.jstest.insertOne(
  	{
  		name: 'test', 
  		age:100, 
  		class:'de'
  	}
  )
  
  > db.jstest.insertOne(
  	{
  		name: 'mongo',
  		class: 'db'
  	}
  )
  
  
  > var lee = {
  				name:'lee-ss',
  				midterm:
  					{kor: 70, eng: 100},
  				final:
  					{kor: 100, eng: 90, math: 20, sci: 50},
  				class: 'de
  			}
  
  > db.multi.insertOne(lee)
  ```

- db.collection.insertMany( [ document1, document2, ... ] )

  ```
  > db.multi.insertMany(
  	[
  		{name: 'kim-sd', class: 'ds', kor: 100, eng: 40, math: 100},
  		{name: 'kang-hd', class: 'ds', kor: 88, eng: 50, math: 70}
  	]
  )
  ```

- db.collection.find( query, projection )

  - query : query selector
  - projection : 출력할 field 선택

  ```
  > db.multi.find({}, {_id:0, name:1})
  { "name" : "hong-gd" }
  { "name" : "lee-ss" }
  { "name" : "kim-sd" }
  { "name" : "kang-hd" }
  
  > db.multi.find({}, {_id:0, name:true, midterm:1})
  { "name" : "hong-gd", "midterm" : { "kor" : 100, "eng" : 60, "math" : 80 } }
  { "name" : "lee-ss", "midterm" : { "kor" : 70, "eng" : 100 } }
  { "name" : "kim-sd" }
  { "name" : "kang-hd" }
  
  > db.multi.find(
  	{'midterm.kor':
  		{$gt:50}
  	}
  )
  
  // 정렬 (1 : asc, -1 : desc)
  > db.multi.find().sort({name : 1})
  
  // 제한
  > db.multi.find().sort({kor:1}).limit(1)
  
  // skip
  > db.multi.find().skip(1)
  
  > db.myfriends.find().pretty()
  ```

  - cursor : 한 번 사용하면 삭제(소모)됨

    ```
    > var cursor = db.multi.find() (한 번 쓰면 메모리 삭제됨)
    > cursor
    { "_id" : ObjectId("622946a1aba64396557e6109"), "name" : "hong-gd", "class" : "de", "midterm" : { "kor" : 100, "eng" : 60, "math" : 80 } }
    { "_id" : ObjectId("62294714aba64396557e610a"), "name" : "lee-ss", "midterm" : { "kor" : 70, "eng" : 100 }, "final" : { "kor" : 100, "eng" : 90, "math" : 20, "sci" : 50 }, "class" : "de" }
    { "_id" : ObjectId("62294783aba64396557e610b"), "name" : "kim-sd", "class" : "ds", "kor" : 100, "eng" : 40, "math" : 100 }
    { "_id" : ObjectId("62294783aba64396557e610c"), "name" : "kang-hd", "class" : "ds", "kor" : 88, "eng" : 50, "math" : 70 }
    > cursor
    
    ```

- db.collection.update( filter, update, options )

  ```
  > db.multi.update(
  	{final:
  		{$exists: true}}, 
  	{$set:
  		{class: 'job'}}
  )
  WriteResult({ "nMatched" : 1, "nUpserted" : 0, "nModified" : 1 })
  ```

- db.collection.updateOne( filter, update, options )

  - filter : 수정할 document를 find(조건)
  - update : update operator or aggregation pipeline
  - options : upsert, writeConcern, ...

  ```
  > db.multi.updateOne(
  	{name:/hong/},
  	{$set:
  		{name: '홍길동'}}
  )
  { "acknowledged" : true, "matchedCount" : 1, "modifiedCount" : 1 }
  
  // updateOne을 사용하여, 아이언맨의 친구에 캡틴아메리카, 블랙위도우 추가
  > db.myfriends.updateOne(
  	{name : 'ironman'},
  	{$push: 
  		{buddy :
  			{$each : ['cptAmerica', 'blackwidow']}
  		}
  	}
  )
  
  // updateOne을 사용하여, 슈퍼맨 친구 중 가장 뒤에 있는 친구를 빼자
  > db.myfriends.updateOne(
  	{name : 'superman'},
  	{$pop : { buddy : 1 }}
  )
  ```

- db.collection.updateMany( filter, update, options )

  ```
  > db.multi.updateMany(
  	{midterm:
  		{$exists: true}},
  	{$set :
  		{class: 'graduated'}}
  )
  { "acknowledged" : true, "matchedCount" : 2, "modifiedCount" : 2 }
  
  // 국어점수가 60점 이하인 사람 모두 찾아서 0점으로 교체
  > function updateKor(){
  	var tmp = db.multi.updateMany({kor: {$lte: 60}}, {$set: {kor: 0}})
  	return tmp
  }
  
  > updateKor()
  { "acknowledged" : true, "matchedCount" : 0, "modifiedCount" : 0 }
  ```

- db.collection.replaceOne( filter, update, options )

  ```
  > db.multi.replaceOne(
  	{final:
  		{$exists: true}},
  	{class: 'job'}
  )
  { "acknowledged" : true, "matchedCount" : 1, "modifiedCount" : 1 }
  ```

- db.collection.deleteOne( filter, options )

  - filter : 삭제할 document를 find
  - options : collation, wirteConcern, ...

  ```
  > db.multi.deleteOne({name : '홍길동'})
  { "acknowledged" : true, "deletedCount" : 1 }
  ```

- db.collection.deleteMany( filter, options )

  ```
  > db.multi.deleteMany({class: {$exists: true}})
  { "acknowledged" : true, "deletedCount" : 3 }
  ```


## Aggregation

- collection이 각 stage를 거치면서 document 처리 및 집계

- 일부 처리는 shard에 대응 ( 각 shard에서 처리 )

- pipeline : 이전 단계의 결과를 다음 단계의 입력으로 사용

  ![image](https://user-images.githubusercontent.com/87686562/157586697-e823ebae-af84-4cfe-a260-f5f060c8b209.png)

  | SQL      | NOSQL    |
  | -------- | -------- |
  | WHERE    | $match   |
  | HAVING   | $match   |
  | GROUP BY | $group   |
  | SELECT   | $project |
  | ORDER BY | $sort    |
  | LIMIT    | $limit   |
  | SUM      | $sum     |
  | COUNT    | $sum     |

  ```
  // collection 생성
  db.multi.insertMany(
  	[
  		{name: 'hong-gd', kor: 100, eng: 30, math: 60},
  		{name: 'kim-sd', kor: 40, eng: 70, math: 100},
  		{name: 'park-jy', kor: 100, eng: 100, math: 100},
  		{name: 'heo-jy', kor: 100, eng: 100, math: 100},
  		{name: 'hong-gd', kor: 60, eng: 100, math: 70},
  	]
  )
  
  db.multi.aggregate(
  	{$match:
  		{kor: {$gt: 70}}},
  	{$project:
  		{kor: 1}},
  	{$group:
  		{_id: "test", "average": {$avg: "$kor"}}}
  )
  { "_id" : "test", "average" : 100 }
  
  db.multi.aggregate(
  	{$match:
      	{name: /s/}},
      {$group:
      	{_id: "test", "sum": {$sum: "$kor"}}}
  )
  { "_id" : "test", "sum" : 40 }
  
  db.score.insertMany(
      [
          {name:"홍길동",kor:90,eng:80,math:98,test:"midterm"},
          {name:"이순신",kor:100,eng:100,math:76,test:"final"},
          {name:"김선달",kor:80,eng:55,math:67,test :"midterm"},
          {name:"강호동",kor:70,eng:69,math:89,test:"midterm"},
          {name:"유재석",kor:60,eng:80,math:78,test:"final"},
          {name:"신동엽",kor:100,eng:69,math:89,test:"midterm"},
          {name:"조세호",kor:75,eng:100,math:100,test:"final"}
      ]
  )
  
  db.score.aggregate(
  	{$project:
      	{_id:0, name:1, kor:1, eng: 1, math: 1}}
  )
  
  db.score.aggregate(
  	{$match:
      	{kor: {$gt: 80}}}
  )
  
  db.score.aggregate(
  	{$group:
      	{_id: "$test", "average": {$avg: "$kor"}}}
  )
  ```


## MapReduce

- Aggregation framework가 처리하지 못하는 복잡한 집계 작업에 사용
- Javascript function을 사용하여 복잡한 작업 처리
- shard에 대응 -> 분산 처리 가능
- query -> map -> reduce -> out
  - map : data mapping ( grouping )
  - reduce : 집계 연산 실행
  - query : 입력될 document
  - out : collection or document 출력

```javascript
function myMap(){
    emit(
        	this.score,
        	{name: this.name, kor: this.kor, eng: this.eng, test: this.test}
    	)
}

function myReduce(key, values){
    var result = {name: new Array(),
                  kor: new Array(),
                  eng: new Array(),
                  total: new Array(),
                 }
    values.forEach(function(val){
        if(val.test == 'final'){
            result.name += val.name + " "
            result.kor += val.kor + " "
            result.eng += val.eng + " "
            result.total += val.kor + val.eng + " "
        }
    })
    return result
}

db.score.mapReduce(myMap, myReduce, {out: {replace: "myRes"}})
db.myRes.find()
```

## Geospatial

```json
db.starbucks02.createIndex({location:"2dsphere"})
// 내 위치 : 37.5248171381127, 127.05505428317193

// 내 위치 기준 주변 검색
db.starbucks02.find(
    {
        location: {
            $near: {
                $geometry:{
                    type: "Point",
                    coordinates: [127.05505428317193, 37.5248171381127]
                },
                $maxDistance: 500
            }
        }
    }
)

// 현재 위치부터 ~ "서울" 단어가 포함된 좌표들의 거리
db.starbucks02.aggregate(
    [
        {
            $geoNear:{
                near:{
                    type: "Point",
                    coordinates : [127.05505428317193, 37.5248171381127]
                },
                spherical : true,
                query: {s_name: /서울/},
                distanceField: "distance"
            }
        }
    ]
)

// 평면 내 검색
// 강남 : 127.02761159460194, 37.49803675628153
// 선정릉 : 127.04391325768417, 37.510487444168355
// 학여울 : 127.07050608281472, 37.496836198102905
db.starbucks02.find(
    {
        location:{
            $geoIntersects: {
                $geometry: {
                    type: "Polygon",
                    coordinates: [
                                    [
                                        [127.02761159460194, 37.49803675628153],
                                        [127.04391325768417, 37.510487444168355],
                                        [127.07050608281472, 37.496836198102905],
                                        [127.02761159460194, 37.49803675628153]
                                    ]
                    ]
                }
            }
        }
    }
)

// 원
db.starbucks02.find(
    {
        location: {
            $geoWithin: {
                $centerSphere: [[127.05505428317193, 37.5248171381127], 0.5/3963.2]
            }
        }
    }
)
```

