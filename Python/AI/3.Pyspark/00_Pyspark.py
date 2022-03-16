from pyspark import SparkConf, SparkContext

conf = SparkConf().setAppName("practice")
sc = SparkContext(conf=conf)

rdd01 = sc.range(0, 1000, 1, 2)
rdd01.collect()
rdd01.getNumPartitions()
rdd01.take(5)

rdd02 = rdd01.filter(lambda x: x % 2)
rdd03 = rdd01.filter(lambda x: not x % 2)

countries = ['korea', 'united states america', 'united kingdom', 
	        'japan', 'france', 'germany', 'italia', 'canada', 'korea']

g8 = sc.parallelize(countries, 2)
g8.count()
g8 = g8.distinct()
g8_upper = g8.map(lambda x: x.upper())
g8_list01 = g8.map(lambda x: list(x))
g8_list02 = g8.flatMap(lambda x: list(x))

counting = sc.range(1, 9, 1, 2)
counting_g8 = counting.zip(g8)

score = [("kang", 10), ("yoo", 30), ("kang", 30), ("shin", 70), ("yoo", 60)]
score_rdd = sc.parallelize(score, 2)
score_rdd_rbk = score_rdd.reduceByKey(lambda x, y: x + y)

nums = sc.parallelize([1, 2, 3, 1, 1, 2, 5, 4], 2)
nums.sortBy(lambda x: x).collect()

arrs = g8.glom()
arrs.collect()

g8.first()
g8.take(3)
g8.takeOrdered(3)
g8.top(3)
g8.countByValue()

nums.max()
nums.min()
nums.mean()
nums.variance()
nums.stdev()
nums.stats()
nums.countByValue()

rdd02_sum = rdd02.sum()
rdd03_sum = rdd03.sum()
rdd02_fold = rdd02.fold(0, lambda x, y: x + y)
rdd02_reduce = rdd02.reduce(lambda x, y: x + y)

def g8Max(x, y):
    if len(x) > len(y):
        return x
    else:
        return y

g8_max_length = g8.reduce(g8Max)
g8_min_length = g8.reduce(lambda x, y: x if len(x) < len(y) else y)

key = g8.keyBy(lambda x: x[0])
key.keys().collect()
key.values().collect()

key.mapValues(lambda x: list(x)).collect()
key.flatMapValues(lambda x: list(x)).collect()

key.groupByKey().mapValues(lambda x: list(x)).collect()
key.groupByKey().mapValues(lambda x: len(x)).collect()

key.reduceByKey(lambda x, y: x + ", " + y).collect()
key.countByKey()

g8.saveAsTextFile("/tmp/g8")

result = sc.textFile("/tmp/g8/part-000*")
result.collect()