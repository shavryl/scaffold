from pyspark.sql.types import StructField, StructType, StringType, LongType
from pyspark.context import SparkContext
from pyspark.sql.session import SparkSession
from pyspark.sql.functions import expr, broadcast
from pyspark.sql import Row


sc = SparkContext('local')
spark = SparkSession(sc)


csvFile = spark.read.format("csv")\
    .option("header", "true")\
    .option("mode", "FAILFAST")\
    .option("inferSchema", "true")\
    .load("data/2010-summary.csv")

csvFile.write.format("csv").mode("overwrite").option("sep", "\t")\
    .save("/tmp/my-tsv-file.tsv")

spark.read.format("json")\
    .option("mode", "FAILFAST")\
    .option("inferSchema", "true")\
    .load("data/2010-summary.json")

csvFile.write.format("json").mode("overwrite").save("/tmp/my-json-file.json")

spark.read.format("parquet")\
    .load("data/2010-summary.parquet")

# driver = "org.sqlite.JDBC"
# path = "data/my-sqlite.db"
# url = "jdbc:sqlite:" + path
# tablename = "flight_info"
#
# dbDataFrame = spark.read.format("jdbc")\
#     .option("url", url)\
#     .option("dbtable", tablename)\
#     .option("driver", driver).load()

# advanced partitioning
# csvFile.limit(10).write.mode("overwrite").partitionBy("DEST_COUNTRY_NAME")\
#     .save("/tmp/partitioned-files.parquet")


spark.sql("SELECT 1 + 1").show()











