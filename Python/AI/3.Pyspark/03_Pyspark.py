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

retails = spark.read.format("csv").option("header", "true").option("inferSchema", "true").load("/home/jngmk/data/retails/*.csv")

from pyspark.sql.functions import to_date, col

date_df = retails.withColumn("date", to_date(col("InvoiceDate"), "yyyy-MM-dd HH:mm:ss"))
date_df.show(3)

notnull_df = date_df.drop()
notnull_df.createOrReplaceTempView("notnullDf")

spark.sql("""
SELECT
    CustomerID, StockCode, SUM(Quantity)
FROM notnullDf
GROUP BY CustomerID, StockCode
ORDER BY CustomerID DESC, StockCode DESC
""").show()

from pyspark.sql.functions import sum, expr

rollup_df = notnull_df.rollup("Date", "Country").agg(sum("Quantity")).selectExpr("Date", "Country", "`SUM(Quantity)` AS total_quantity").orderBy("Date")
rollup_df.show()
rollup_df.where("Country IS NULL").show()

cube_df = notnull_df.cube("Date", "Country").agg(sum(col("Quantity"))).select("Date", "Country", "SUM(Quantity)").orderBy("Date")
cube_df.where("Date IS NULL").show()

person = spark.createDataFrame(
    [
        (1, "shin dongyeup", 2, [1]),
        (2, "seo janghoon", 3, [2]),
        (3, "yoo jaeseok", 1, [1, 2]),
        (4, "kang hodong", 0, [0])
    ]
).toDF("id", "name", "program", "job")

program = spark.createDataFrame(
    [
        (1, "MBC", "놀면 뭐하니"),
        (2, "KBS", "불후의 명곡"),
        (3, "SBS", "미운 우리 새끼"),
        (4, "JTBC", "뭉쳐야 찬다")
    ]
).toDF("id", "broadcaster", "program")

job = spark.createDataFrame(
    [
        (1, "main mc"),
        (2, "member")
    ]
).toDF("id", "job")

person.show()
program.show()
job.show()

person.createOrReplaceTempView("person")
program.createOrReplaceTempView("program")
job.createOrReplaceTempView("job")

# person.join(program, person['program'] == program['id']).show()
person.join(program, person.program == program.id).show()
spark.sql("""
SELECT *
FROM PERSON PS
    JOIN PROGRAM PR
    ON PS.PROGRAM = PR.ID
""").show()

conditions = person.program == program.id
person.join(program, conditions, "inner").show()
person.join(program, conditions, "outer").show()
spark.sql("""
SELECT *
FROM PERSON PS
    FULL OUTER JOIN PROGRAM PR
    ON PS.PROGRAM = PR.ID
""").show()

person.join(program, conditions, "left_outer").show()
person.join(program, conditions, "right_outer").show()
person.join(program, conditions, "left_anti").show()
person.join(program, conditions, "left_semi").show()
# person.join(program, how = "cross").show()
person.crossJoin(program).show()
# person.join(job, expr("array_contains(job, id)")).show()
person.withColumnRenamed("id", "num").withColumnRenamed("job", "role").join(job, expr("array_contains(role, id)")).show()

spark.sql("""
SELECT P.*
FROM PERSON P
    JOIN PROGRAM M
    ON P.PROGRAM = M.ID
WHERE BROADCASTER = 'SBS'
""").show()

spark.sql("""
SELECT *
FROM PERSON
WHERE PROGRAM = (SELECT ID FROM PROGRAM WHERE BROADCASTER = 'SBS')
""").show()