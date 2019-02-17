from pyspark.sql.types import StructField, StructType, StringType, LongType
from pyspark.context import SparkContext
from pyspark.sql.session import SparkSession
from pyspark.sql.functions import expr, col, column, lit, desc, asc
from pyspark.sql import Row


sc = SparkContext('local')
spark = SparkSession(sc)


myManualSchema = StructType([
    StructField("DEST_COUNTRY_NAME", StringType(), True),
    StructField("ORIGIN_COUNTRY_NAME", StringType(), True),
    StructField("count", LongType(), False, metadata={"hello": "world"})
])
# sortWithPartitions - optimization
df = spark.read.format("json").schema(myManualSchema)\
    .load("data/2015-summary.json").sortWithinPartitions("count")

schema = df.schema

newRows = [
    Row("New Country", "Other Country", 1),
    Row("New Country 2", "Other Country 3", 1)
]
parallelizedRows = spark.sparkContext.parallelize(newRows)
newDF = spark.createDataFrame(parallelizedRows, schema)

# append df with new rows by union
df.union(newDF)\
    .where("count = 1")\
    .where(col("ORIGIN_COUNTRY_NAME") != "United States")\
    .show(1)

df.rdd.getNumPartitions()

df.repartition(5, col("DEST_COUNTRY_NAME")).coalesce(2)

collectDF = df.limit(10)
collectDF.take(5)
collectDF.show(5, False)
# returns an iterator !
tt = list(collectDF.toLocalIterator())
for t in tt:
    print(t)
