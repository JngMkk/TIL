from pyspark import SparkConf, SparkContext
import sys, re

conf = SparkConf().setAppName("Word Count")
sc = SparkContext(conf=conf)

if len(sys.argv) != 3:
    print("wordcount.py input_file output_dir 형식으로 입력")
    sys.exit(0)
else:
    inputfile = sys.argv[1]
    outputdir = sys.argv[2]

wordcount = sc.textFile(inputfile)\
    .repartition(10)\
        .filter(lambda x: len(x) > 0)\
            .flatMap(lambda x: re.split('\W+', x))\
                .filter(lambda x: len(x) > 0)\
                    .map(lambda x: (x.lower(), 1))\
                        .reduceByKey(lambda x, y: x + y)\
                            .map(lambda x: (x[1], x[0]))\
                                .sortByKey(ascending= False)\
                                    .persist()

wordcount.saveAsTextFile(outputdir)
top10 = wordcount.take(5)
result = []
for counts in top10 :
    result.append(counts[1])
print(result)