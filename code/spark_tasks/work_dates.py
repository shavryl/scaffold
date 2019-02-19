from pyspark.context import SparkContext
from pyspark.sql.session import SparkSession
from pyspark.sql.functions import (
    date_add, date_sub, col, lit,
    current_timestamp, current_date,
    datediff, months_between, to_date,
    to_timestamp)


sc = SparkContext('local')
spark = SparkSession(sc)

df = spark.read.format("csv")\
    .option("header", "true")\
    .option("inferSchema", "true")\
    .load("data/2010-12-01.csv")
df.createOrReplaceTempView("dfTable")

dateDF = spark.range(10)\
    .withColumn("today", current_date())\
    .withColumn("now", current_timestamp())
dateDF.createOrReplaceTempView("dateTable")

# add and substract 5 days in new columns
dateDF.select(date_sub(col("today"), 5), date_add(col("today"), 5)).show(1)

# get the number days between dates
dateDF.withColumn("week_ago", date_sub(col("today"), 7))\
    .select(datediff(col("week_ago"), col("today"))).show(1)

# get months between custom dates
# to_date converts string in java-simple-date-format
# into date format
dateDF.select(
    to_date(lit("2016-01-01")).alias("start"),
    to_date(lit("2017-05-22")).alias("end"))\
    .select(months_between(col("start"), col("end"))).show(1)

# spark returns null silently if date format is wrong
dateDF.select(to_date(lit("2016-20-12")), to_date(lit("2017-12-11"))).show(1)

# robust way to do it
dateFormat = "yyyy-dd-MM"
cleanDateDF = spark.range(1).select(
    to_date(lit("2017-12-11"), dateFormat).alias("date"),
    to_date(lit("2017-20-12"), dateFormat).alias("date2"))
cleanDateDF.createOrReplaceTempView("dataTable2")

cleanDateDF.select(to_timestamp(col("date"), dateFormat)).show()
