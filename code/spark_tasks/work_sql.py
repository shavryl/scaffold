from pyspark.sql.types import StructField, StructType, StringType, LongType
from pyspark.context import SparkContext
from pyspark.sql.session import SparkSession
from pyspark.sql.functions import expr, broadcast
from pyspark.sql import Row


sc = SparkContext('local')
spark = SparkSession(sc)


spark.read.json("data/2015-summary.json")\
    .createOrReplaceTempView("flights")

spark.sql("""SELECT DEST_COUNTRY_NAME, sum(count)
    FROM flights GROUP BY DEST_COUNTRY_NAME""")\
    .where("DEST_COUNTRY_NAME like 'S%'")\
    .where("`sum(count)` > 10")\
    .collect()

spark.sql("""CREATE TEMPORARY VIEW nested_data AS
  SELECT (DEST_COUNTRY_NAME, ORIGIN_COUNTRY_NAME) as country, count FROM flights
""")

# to query individual columns within a struct use dot syntax
spark.sql("""SELECT country.DEST_COUNTRY_NAME,
 count FROM nested_data""")\
    .show(20, False)

# you can also select all the subvalues from a struct by using
# the structs name and select all of the subcolumns, although
# these aren't truly subcolumns it does provide a simpler way to
# think about them because we can do everything that we like as
# if they were a column:
spark.sql("""SELECT country.*, count FROM nested_data""").show()











