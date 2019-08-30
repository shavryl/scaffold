from pyspark.context import SparkContext
from pyspark.sql.session import SparkSession
from pyspark.sql.functions import (
    date_add, date_sub, col, lit,
    current_timestamp, current_date,
    datediff, months_between, to_date,
    to_timestamp, coalesce, struct,
    split, size, array_contains, explode,
    create_map,
)


sc = SparkContext('local')
spark = SparkSession(sc)

df = spark.read.format("csv")\
    .option("header", "true")\
    .option("inferSchema", "true")\
    .load("data/2010-12-01.csv")
df.createOrReplaceTempView("dfTable")


df.selectExpr("(Description, InvoiceNo) as complex", "*")


complexDF = df.select(struct("Description", "InvoiceNo").alias("complex"))
complexDF.createOrReplaceTempView("complexDF")

#to query we use dot syntax
complexDF.select("complex.Description")

# query with getfield
complexDF.select(col("complex").getField("Description"))

# query values in the struct
complexDF.select("complex.*")

df.select(split(col("Description"), " "))

# select firsts word from description for all rows
df.select(split(col("Description"), " ").alias("array_col"))\
    .selectExpr("array_col[0]").show()

# count words after split in every row
df.select(size(split(col("Description"), " ")))

# returns boolean
df.select(array_contains(split(col("Description"), " "), "WHITE"))

# explode takes a column that consists of arrays
# and creates one row per value in the array
df.withColumn("splitted", split(col("Description"), " "))\
    .withColumn("exploded", explode(col("splitted")))\
    .select("Description", "InvoiceNo", "exploded")

# map func and key-value pairs of columns
df.select(create_map(col("Description"), col("InvoiceNo")).alias("complex_map"))

# select value by key from map
df.select(create_map(col("Description"), col("InvoiceNo")).alias("complex_map"))\
    .selectExpr("complex_map['WHITE METAL LANTERN']")

# explode map functions to columns
df.select(create_map(col("Description"), col("InvoiceNo")).alias("complex_map"))\
    .selectExpr("explode(complex_map)").show(50, False)
