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
 count FROM nested_data""")

# you can also select all the subvalues from a struct by using
# the structs name and select all of the subcolumns, although
# these aren't truly subcolumns it does provide a simpler way to
# think about them because we can do everything that we like as
# if they were a column:
spark.sql("""SELECT country.*, count FROM nested_data""")

# collect_list function creates a list of values
# collect_set function creates an array without duplicates
spark.sql("""SELECT DEST_COUNTRY_NAME as new_name,
    collect_list(count) as flight_counts,
    collect_set(ORIGIN_COUNTRY_NAME) as origin_set
    FROM flights GROUP BY DEST_COUNTRY_NAME""")

# create array manually within a column
spark.sql("""SELECT DEST_COUNTRY_NAME, ARRAY(1, 2, 3) FROM flights""")

# querry list by position
spark.sql("""SELECT DEST_COUNTRY_NAME as new_name,
    collect_list(count)[0] as first_element
    FROM flights GROUP BY DEST_COUNTRY_NAME""")


# convert an array back into rows, you do this by using explode func
spark.sql("""CREATE OR REPLACE TEMP VIEW flights_agg AS
    SELECT DEST_COUNTRY_NAME, collect_list(count) as collected_counts
    FROM flights GROUP BY DEST_COUNTRY_NAME""")

originalDF = spark.sql("""SELECT explode(collected_counts),
    DEST_COUNTRY_NAME FROM flights_agg""")

# list of SQL functions
spark.sql("""SHOW FUNCTIONS""")

# SHOW SYSTEM FUNCTIONS
# SHOW USER FUNCTIONS
# SHOW FUNCTIONS "s*";
# DESCRIBE returns info