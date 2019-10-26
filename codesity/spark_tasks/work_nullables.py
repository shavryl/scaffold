from pyspark.context import SparkContext
from pyspark.sql.session import SparkSession
from pyspark.sql.functions import (
    date_add, date_sub, col, lit,
    current_timestamp, current_date,
    datediff, months_between, to_date,
    to_timestamp, coalesce)


sc = SparkContext('local')
spark = SparkSession(sc)

df = spark.read.format("csv")\
    .option("header", "true")\
    .option("inferSchema", "true")\
    .load("data/2010-12-01.csv")
df.createOrReplaceTempView("dfTable")

df.select(coalesce(col("Description"), col("CustomerId"))).show(1)

# specify drop columns with null
df.na.drop("all", subset=["StockCode", "InvoiceNo"])

df.na.fill("All null values become this string").show(1)

# column name to value
fill_cols_vals = {"StockCode": 5, "Description": "No Value"}
df.na.fill(fill_cols_vals)

# replace value should be the same type as original value
df.na.replace([""], ["UNKNOWN"], "Description")

