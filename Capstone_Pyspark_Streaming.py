from pyspark.streaming import StreamingContext
from pyspark import SparkConf, SparkContext
conf = SparkConf().setAppName("Capstone")
sc = SparkContext.getOrCreate(conf=conf)
ssc = StreamingContext(sc,1)
rdd = ssc.textFileStream("/home/ravi/test/")
rdd.pprint()
ssc.start()
ssc.awaitTerminationOrTimeout(1)
