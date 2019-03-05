from pyspark.sql.types import StructField, StructType, StringType, LongType
from pyspark.context import SparkContext
from pyspark.sql.session import SparkSession
from pyspark.sql.functions import expr, broadcast
from pyspark.sql import Row


sc = SparkContext('local')
spark = SparkSession(sc)


spark.read.json("data/2015-summary.json")\
    .createOrReplaceTempView("some_sql_view")

spark.sql("""SELECT DEST_COUNTRY_NAME, sum(count)
    FROM some_sql_view GROUP BY DEST_COUNTRY_NAME""")\
    .where("DEST_COUNTRY_NAME like 'S%'")\
    .where("`sum(count)` > 10")\
    .collect()
