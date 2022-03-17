from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession

conf = SparkConf().setAppName("practice")
sc = SparkContext(conf=conf)
spark = SparkSession.builder.master("yarn").appName("practice").getOrCreate()

multi = spark.read.format("csv").option("header", "true").load("/home/jngmk/all.csv")
multi.count()
multi.createOrReplaceTempView("multi")
multi.show(multi.count())

from pyspark.sql.functions import col

multi.groupBy("chat_from").count().orderBy(col("count").desc()).show()

multi.where(col("chat_to") == "이동헌강사").groupBy("chat_from", "chat_to").count().orderBy(col("count").desc()).show()
spark.sql("""
SELECT CHAT_FROM, CHAT_TO, COUNT(*)
FROM MULTI
WHERE CHAT_TO = "이동헌강사"
GROUP BY CHAT_FROM, CHAT_TO
ORDER BY 3 DESC
""").show()

from pyspark.sql.functions import substring

multi.groupBy(substring("chat_time", 1, 2)).count().orderBy(substring("chat_time", 1, 2)).show()
spark.sql("""
SELECT
    SUBSTRING(CHAT_TIME, 1, 2),
    COUNT(*)
FROM MULTI
GROUP BY SUBSTRING(CHAT_TIME, 1, 2)
ORDER BY 1
""").show()

# 날짜 별 채팅 횟수
multi.groupBy(col("chat_date")).count().orderBy(col("chat_date")).show()
spark.sql("""
SELECT CHAT_DATE, COUNT(*)
FROM MULTI
GROUP BY CHAT_DATE
ORDER BY 1
""").show()

# 날짜와 시간 별 채팅 횟수
multi.groupBy("chat_date", substring("chat_time", 1, 2)).count().orderBy("chat_date", substring("chat_time", 1, 2)).show()

hour_chat = multi.groupBy(substring("chat_time", 1, 2).alias("hour"), "chat_from").count().orderBy(substring("chat_time", 1, 2), col("count").desc())
hour_chat.show(hour_chat.count())
hour_chat.write.format("csv").mode("overwrite").save("hour_chat")
hour_chat.coalesce(1).write.format("csv").mode("overwrite").save("/home/jngmk/hour_chat")

# mysql 연결
user="root"
password="1234"
url="jdbc:mysql://localhost:3306/mysql"
driver="com.mysql.cj.jdbc.Driver"
dbtable="test"

test_df = spark.read.format("jdbc").options(user=user, password=password, url=url, driver=driver, dbtable=dbtable).load()
test_df.show()

test_insert = [(3, "mysql"), (4, "zeppelin")]
insert_df = sc.parallelize(test_insert).toDF(["id", "name"])
insert_df.write.jdbc(url, dbtable, "append", properties={"driver": driver, "user": user, "password" : password})
test_df.show()

# mongo 연결
# pyspark --packages org.mongodb.spark:mongo-spark-connector_2.12:3.0.1
test = spark.read.format("mongo").option("database", "test").option("collection", "test").load()
test.show()
insert_df = spark.createDataFrame([("11", "mongo-spark")], ["id", "name"])
insert_df.show()
insert_df.write.format("mongo").option("database", "test").option("collection", "test").mode("append").save()
test.show()