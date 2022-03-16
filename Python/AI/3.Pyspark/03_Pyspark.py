from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession

conf = SparkConf().setAppName("practice")
sc = SparkContext(conf=conf)
spark = SparkSession.builder.getOrCreate()

csv_file01 = spark.read.format("csv").option("header", "true").load("/home/jngmk/data/flights/csv/2010-summary.csv")
csv_file02 = spark.read.option("header", "true").csv("/home/jngmk/data/flights/csv/2010-summary.csv")
csv_file02.head(4)

# dataframe.write.mode : append, overwrite, error/errorifexists, ignore
csv_file02.write.format("csv").mode("overwrite").save("/tmp/csv")
# hdfs dfs -ls /tmp/csv
# hdfs dfs -cat /tmp/csv/*.csv

json_file01 = spark.read.format("json").load("/home/jngmk/data/flights/json/2010-summary.json")
json_file01.show(5)
json_file01.write.format("json").mode("append").save("/tmp/json")

"""

parquet : spark 컬럼 기반 데이터 저장 방식
orc : hadoop 컬럼 기반 데이터 저장 방식
text
db

"""