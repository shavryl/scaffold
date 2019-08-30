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

# query is uncorrelated because it does not include any
# information from the outer scope of the query
spark.sql("""SELECT * FROM flights
    WHERE origin_country_name IN (SELECT dest_country_name FROM flights
        GROUP BY dest_country_name ORDER BY sum(count) DESC LIMIT 5)
""")

# correlated predicate subqueries allow you to use
# information from the outer scope in your inner query
spark.sql("""SELECT * FROM flights f1
    WHERE EXISTS (SELECT 1 FROM flights f2
        WHERE f1.dest_country_name = f2.origin_country_name)
    AND EXISTS (SELECT 1 FROM flights f2
        WHERE f2.dest_country_name = f1.origin_country_name)
""")

# using uncorrelated scalar queries you can bring in some supplemental
# information that you might not have previously. For example if you
# wanted to include the maximum value as its own column :
spark.sql("""SELECT *, (SELECT max(count) FROM flights)
    AS maximum FROM flights""").show()




















