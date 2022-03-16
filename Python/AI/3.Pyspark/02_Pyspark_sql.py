from pyspark import SparkConf, SparkContext

conf = SparkConf().setAppName("practice")
sc = SparkContext(conf=conf)

from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

f2015 = spark.read.format("json").load("/home/jngmk/data/flights/json/2015-summary.json")
f2015.show()
f2015.show(5)
f2015.show(f2015.count())
f2015.createOrReplaceTempView("flights2015")

sqls = spark.sql("""
SELECT
	DEST_COUNTRY_NAME,
	COUNT(1)
FROM flights2015
GROUP BY DEST_COUNTRY_NAME
""")

sqls.show()

dfs = f2015.groupBy("DEST_COUNTRY_NAME").count()
dfs.show()

sqls.explain()
dfs.explain()

spark.sql("SELECT MAX(COUNT) FROM flights2015").take(1)

from pyspark.sql.functions import max

f2015.select(max("count")).take(1)

f2015.select("DEST_COUNTRY_NAME").show(5)

spark.sql("SELECT DEST_COUNTRY_NAME FROM flights LIMIT 5").show()

from pyspark.sql.functions import expr, col

f2015.select(expr("DEST_COUNTRY_NAME"), col("DEST_COUNTRY_NAME")).show(5)

f2015.select(expr("DEST_COUNTRY_NAME AS destination")).show(5)

f2015.select(col("DEST_COUNTRY_NAME").alias("destination")).show(5)

spark.sql('SELECT DEST_COUNTRY_NAME AS destination FROM flights2015 LIMIT 5').show()

f2015.selectExpr("DEST_COUNTRY_NAME AS destination").show(5)

f2015.selectExpr("*", "(DEST_COUNTRY_NAME = ORIGIN_COUNTRY_NAME) AS domestic_flight").show()

spark.sql("SELECT AVG(COUNT), COUNT(DISTINCT(DEST_COUNTRY_NAME)) FROM filghts2015").show()

f2015.selectExpr("AVG(COUNT)", "COUNT(DISTINCT(DEST_COUNTRY_NAME))").show()

from pyspark.sql.functions import lit

f2015.select(expr("*"), lit(1).alias("one")).show(5)

spark.sql("SELECT *, 1 AS one FROM fligths2015 LIMIT 5").show()

f2015.withColumn("DOMESTIC_FLIGHT", expr("DEST_COUNTRY_NAME = ORIGIN_COUNTRY_NAME")).show()

f2015.withColumnRenamed("DEST_COUNTRY_NAME", "DESTINATION").show()

f2015.drop("count").show()

f2015.drop("count").columns

f2015.withColumn("count2", col("count").cast("string")).summary

f2015.withColumn("count2", col("count").cast("string")).show()

spark.sql("SELECT *, CAST(count as string) AS count2 FROM flights2015").show()

f2015.filter(col("count") < 2).show(5)

spark.sql("SELECT * FROM flights2015 WHERE count < 2 LIMIT 5").show()

f2015.where(col("count") < 2).where(col("ORIGIN_COUNTRY_NAME") != "Croatia").show(5)

spark.sql("SELECT * FROM flights2015 WHERE count < 2 AND ORIGIN_COUNTRY_NAME != 'Croatia' LIMIT 5").show()

f2015.select("DEST_COUNTRY_NAME").distinct().count()

spark.sql("SELECT COUNT(DISTINCT DEST_COUNTRY_NAME) AS count FROM flights2015").show()

from pyspark.sql import Row

new_rows = [
    Row("Korea", "Korea", 5),
    Row("Korea", "Wakanda", 1)
]

rdd_rows = sc.parallelize(new_rows)
schema = f2015.schema
df_rows = spark.createDataFrame(rdd_rows, schema)

f2015.union(df_rows).where("count = 1").where(col("ORIGIN_COUNTRY_NAME") != "United States").show()

f2015.sort("count").show(f2015.count())

f2015.orderBy(col("count").asc()).show(f2015.count())

spark.sql("SELECT * FROM flights2015 ORDER BY count desc").show(f2015.count())

f2015.orderBy(col("DEST_COUNTRY_NAME").desc(), col("count").asc()).show(5)

f2015.orderBy(expr("DEST_COUNTRY_NAME DESC"), expr("count asc")).show(5)

spark.sql("SELECT * FROM flights2015 ORDER BY DEST_COUNTRY_NAME DESC, COUNT ASC LIMIT 5").show()

f2015.limit(5).show()

retails = spark.read.format("csv").option("header", "true").option("inferSchema", "true").load("/home/jngmk/data/retails/2010-12-01.csv")

retails.printSchema()

retails.createOrReplaceTempView("retails")
retails.show()

spark.sql("SELECT * FROM RETAILS").show()

retails.where(col("InvoiceNo") != 536365).select("InvoiceNo", "Description").show(5)

retails.where(col("InvoiceNo") != 536365).select("InvoiceNo", "Description").show(5, False)

retails.where("InvoiceNo <> 536365").show(5, False)

from pyspark.sql.functions import instr

priceFilter = col("UnitPrice") > 600
descripFilter = instr(retails.Description, "POSTAGE") >= 1

retails.where(retails.StockCode.isin("DOT")).where(priceFilter | descripFilter).show()

spark.sql("""
SELECT *
FROM retails
WHERE StockCode in ("DOT")
AND (UnitPrice > 600 OR INSTR(Description, "POSTAGE") >= 1)
""").show()

dotCodeFilter = col("StockCode") == "DOT"
priceFilter = col("UnitPrice") > 600
descriptFilter = instr(col("Description"), "POSTAGE") >= 1

retails.withColumn("isExpensive", dotCodeFilter & (priceFilter | descriptFilter)).where("isExpensive").select("UnitPrice", "isExpensive").show(5)

spark.sql("""
SELECT
	UNITPRICE,
	StockCode = 'DOT' AND (UnitPrice > 600 OR INSTR(Description, 'POSTAGE') >= 1) AS isExpensive
FROM retails
WHERE StockCode = 'DOT' AND (UnitPrice > 600 OR INSTR(Description, 'POSTAGE') >= 1)
""").show()

from pyspark.sql.functions import pow

quantity = pow(col("Quantity") * col("UnitPrice"), 2) + 5

retails.select(col("CustomerId"), quantity.alias("myQuantity")).show(5)

spark.sql("""
SELECT
	CustomerId,
	(POWER((Quantity * UnitPrice), 2) + 5) AS myQuantity
FROM retails
""").show(5)

from pyspark.sql.functions import round, bround

retails.select(round(lit('2.5')), bround(lit('2.5')), lit('2.5')).show(5)

spark.sql("""
SELECT ROUND(2.5), BROUND(2.5)
FROM retails
""").show(5)

retails.describe().show()

retails = spark.read.format("csv").option("header", "true").option("inferSchema", "true").load("/home/jngmk/data/retails/2010-12-01.csv") 
retails.createOrReplaceTempView("retails") 

from pyspark.sql.functions import count, mean, stddev_pop, min, max

retails.select(count('UnitPrice'), mean('UnitPrice'), stddev_pop('UnitPrice'), min('UnitPrice'), max('UnitPrice')).show()

from pyspark.sql.functions import monotonically_increasing_id

retails.select("*", monotonically_increasing_id()).show(5)

from pyspark.sql.functions import initcap

retails.select(initcap(col("Description")), col("Description")).show(5, False)

from pyspark.sql.functions import lower, upper

retails.select(col("Description"), lower(col("Description")), upper(col("Description"))).show(5)

from pyspark.sql.functions import ltrim, rtrim, trim, lpad, rpad, lit

retails.select(ltrim(lit("    hello    ")).alias("ltrim"), rtrim(lit("    hello    ")).alias("rtrim"),
trim(lit("    hello    ")).alias("trim"), lpad(lit("hello"), 10, "*").alias("lpad"), rpad(lit("hello"), 10, "*").alias("rpad")).show(1)

from pyspark.sql.functions import regexp_replace

regex_str = "BLACK|WHITE|RED|GREEN|BLUE"
retails.select(col("Description"), regexp_replace(col("Description"), regex_str, "COLOR").alias("color")).show(5, False)

spark.sql("""
SELECT
    Description,
    REGEXP_REPLACE(Description, "BLACK|WHITE|RED|GREN|BLUE", "COLOR") AS COLOR
FROM retails
""").show(5, False)

from pyspark.sql.functions import translate

retails.select(col("Description"), translate(col("Description"), "ABCD", "1234")).show(5, False)

from pyspark.sql.functions import regexp_extract

extract_str = "(BLACK|WHITE|RED|GREEN|BLUE)"
retails.select(col("Description"), regexp_extract(col("Description"), extract_str, 1).alias("extract")).show(5, False)

containsBlack = instr(col("Description"), "BLACK") >= 1
containsWhite = instr(col("Description"), "WHITE") >= 1
retails.withColumn("hasBlackWhite", containsBlack | containsWhite).select("Description", "hasBlackWhite").show(5, False)

from pyspark.sql.functions import current_date, current_timestamp

date_df = spark.range(10).withColumn("today_date", current_date()).withColumn("now_timestamp", current_timestamp())
date_df.show(10, False)

date_df.createOrReplaceTempView("dateTable")
spark.sql("SELECT * FROM dateTable").show()

from pyspark.sql.functions import date_add, date_sub

date_df.select(date_sub(col("today_date"), 5), date_add(col("today_date"), 5)).show()

spark.sql("SELECT DATE_SUB(today_date, 5) AS s, DATE_ADD(today_date, 5) AS a FROM dateTable").show(1)

from pyspark.sql.functions import datediff, months_between, to_date

date_df.withColumn("week_ago", date_sub(col("today_date"), 7)).select(datediff(col("week_ago"), col("today_date"))).show(1)

date_df.select(to_date(lit("2022-03-15")).alias("now"), to_date(lit("2022-05-13")).alias("end")).select(months_between(col("now"), col("end"))).show()

date_df.select(to_date(lit('2022-12-32'))).show(1)

# simpleDateFormat (java)
dateFormat = 'yyyy-dd-MM'
clean_date = spark.range(1).select(to_date(lit('2022-11-12'), dateFormat).alias('date'))
clean_date.show()

null_df = sc.parallelize(
    [
        Row(name='Kang', phone='010-0000-0000', address='Seoul'),
        Row(name='Shin', phone='010-1111-1111', address=None),
        Row(name='Yoo', phone=None, address=None)
    ]
).toDF()
null_df.show()
null_df.createOrReplaceTempView("nullTable")
spark.sql("SELECT * FROM nullTable").show()

from pyspark.sql.functions import coalesce

null_df.select(coalesce(col("address"), col("phone")).alias("coalesce")).show()

"""
ifnull : 첫 번째 값이 null이면 두 번째 값 리턴
nullif : 두 값이 같으면 null
nvl : 첫 번째 값이 null 이면 두 번째 값 리턴
nvl2 : 첫 번째 값이 null이면 두 번째 값, 아니면 세 번째 값
"""

spark.sql("""
SELECT
    IFNULL(NULL, 'VALUE'),
    NULLIF('SAME', 'SAME'),
    NULLIF('SAME', 'NOTSAME'),
    NVL(NULL, 'VALUE'),
    NVL2(NULL, 'VALUE', 'VALUE2'),
    NVL2('NOTNULL', 'VALUE', 'VALUE2')
""").show()

# DataFrameNaFunction : drop, fill, replace
null_df.count()
null_df.na.drop("any").count()
null_df.na.drop("all").count()
null_df.na.drop("all", subset=['phone']).count()
null_df.na.drop("all", subset=['address']).count()
null_df.na.drop("all", subset=['phone','address']).count()

null_df.na.fill("N/A").show()
null_df.na.fill("N/A", subset=["name", "address"]).show()

fill_cols_val = {"phone" : "070-000-0000", "address": "street"}
null_df.na.fill(fill_cols_val).show()

null_df.na.replace(["Seoul"], ["서울"], "address").show()

# 구조체 : dataframe 안에 dataframe
retails.selectExpr("(Description, InvoiceNo) AS complex", "*").show(5, False)

from pyspark.sql.functions import struct

complex_df = retails.select(struct("Description", "InvoiceNo").alias("complex"))
complex_df.createOrReplaceTempView("complexdf")
complex_df.show()
spark.sql("SELECT * FROM complexdf").show()

complex_df.select("complex.Description").show(5, False)
complex_df.select(col("complex").getField("InvoiceNo")).show(5, False)
complex_df.select("complex.*").show(5, False)

from pyspark.sql.functions import split

retails.select(split(col("Description"), " ")).show(5, False)
retails.select(split(col("Description"), " ").alias("arrays")).selectExpr("arrays[0]").show(5)

from pyspark.sql.functions import size

retails.select(size(split(col("Description"), " ")).alias("array_size")).show(5)

from pyspark.sql.functions import array_contains

retails.select(array_contains(split(col("Description"), " "), "WHITE").alias("isWhite")).show(5)

from pyspark.sql.functions import create_map

retails.select(create_map(col("StockCode"), col("Description")).alias("complex_map")).show(5, False)
retails.select(create_map(col("StockCode"), col("Description")).alias("complex_map")).selectExpr("complex_map['84406B']").show()

def power3(value):
    return value ** 3

from pyspark.sql.functions import udf

pow3 = udf(power3)
user_def_df = spark.range(5).toDF("num")
user_def_df.select(col("num"), pow3(col("num"))).show()

retails_all = spark.read.format("csv").option("header", "true").option("inferSchema", "true").load("/home/jngmk/data/retails/*.csv")
retails_all.count()
retails_all.printSchema()

retails_all.createOrReplaceTempView("retailsAll")

retails_all.select(count("StockCode")).show()
spark.sql("SELECT COUNT(*) AS cnt FROM retailsAll").show()

from pyspark.sql.functions import countDistinct

retails_all.select(countDistinct("*").alias("cntDistinct")).show()
spark.sql("SELECT COUNT(DISTINCT(*)) AS CNTDISTINCT FROM RETAILSALL").show()

from pyspark.sql.functions import first, last

retails_all.select(first("StockCode"), last("StockCode")).show()

retails_all.select(min("Quantity"), max("Quantity")).show()

from pyspark.sql.functions import sumDistinct

retails_all.select(sumDistinct("Quantity")).show()

spark.sql("SELECT SUM(DISTINCT(Quantity)) FROM RETAILSALL").show()

from pyspark.sql.functions import avg, sum, count

retails_all.select(count("Quantity").alias("countQuantity"), sum("Quantity").alias("sumQuantity"), avg("Quantity").alias("avgQuantity"), expr("mean(Quantity)").alias("meanQuantity")).show()

"""
분산, 표준편차

var_pop : 모분산
stddev_pop : 모표준편차

var_samp : 표본 분산
stddev_samp : 표본 표준편차
"""

from pyspark.sql.functions import var_pop, stddev_pop, var_samp, stddev_samp

retails_all.select(var_pop("Quantity").alias("varpop"), stddev_pop("Quantity").alias("stddevpop"), var_samp("Quantity").alias("varsamp"), stddev_samp("Quantity").alias("stddevsamp")).show()

"""
공분산, 상관관계
corr : 피어슨 상관관계 (DataFrame.corr과 같음)
covar_pop : 모집단 공분산
covar_samp : 표본집단 공분산
"""

from pyspark.sql.functions import corr, covar_pop, covar_samp

retails_all.select(corr("InvoiceNo", "Quantity").alias("corr"), covar_pop("InvoiceNo", "Quantity").alias("covarpop"), covar_samp("InvoiceNo", "Quantity").alias("covarsamp")).show()
retails_all.select(corr("UnitPrice", "Quantity").alias("corr"), covar_pop("UnitPrice", "Quantity").alias("covarpop"), covar_samp("UnitPrice", "Quantity").alias("covarsamp")).show(1, False)

# agg : aggregate
# collect_set
# collect_list

from pyspark.sql.functions import collect_list, collect_set

retails_all.agg(collect_set("Country").alias("S"), collect_list("Country").alias("L")).select(size("S"), size("L")).show()

retails_all.groupBy("InvoiceNo", "CustomerId").count().show()

spark.sql("""
SELECT INVOICENO, CUSTOMERID, COUNT(*)
FROM RETAILSALL
GROUP BY INVOICENO, CUSTOMERID
""").show()

retails_all.groupBy("InvoiceNo").agg(count("Quantity").alias("quan"), expr("count(Quantity)")).show()

date_df = retails_all.withColumn("date", to_date(col("InvoiceDate"), "yyyy-MM-dd HH:mm:ss"))
date_df.show()
date_df.createOrReplaceTempView("date_df")

from pyspark.sql.window import Window
from pyspark.sql.functions import desc
from pyspark.sql.functions import dense_rank, rank

win_func = Window.partitionBy("CustomerId", "date").orderBy(desc("Quantity")).rowsBetween(Window.unboundedPreceding, Window.currentRow)

max_quantity = max(col("Quantity")).over(win_func)
win_dense_rank = dense_rank().over(win_func)
win_rank = rank().over(win_func)

date_df.where("CustomerId IS NOT NULL").orderBy("CustomerId").select(col("CustomerId"), col("date"), col("Quantity"), win_rank.alias("quantityRank"), win_dense_rank.alias("quantityDense"), max_quantity.alias("quantityMax")).show()