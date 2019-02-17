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


df.orderBy(expr("count desc")).show(5)
# sorting by different columns values
df.orderBy(col("count").desc(), col("DEST_COUNTRY_NAME").asc()).show(5)
