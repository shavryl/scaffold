from pyspark.sql.types import StructField, StructType, StringType, LongType
from pyspark.context import SparkContext
from pyspark.sql.session import SparkSession
from pyspark.sql.functions import *
from pyspark.sql import Row


sc = SparkContext('local')
spark = SparkSession(sc)


df = spark.read.format("csv")\
    .option("header", "true")\
    .option("inferSchema", "true")\
    .load("data/2010-12-01.csv")
df.printSchema()
df.createOrReplaceTempView("dfTable")

# show(vertical=True) makes Row representation
df.where(col("InvoiceNo") != 536365)\
    .select("InvoiceNo", "Description")\
    .show(1, False, True)

priceFilter = col("UnitPrice") > 600
descripFilter = instr(df.Description, "POSTAGE") >= 1
df.where(df.StockCode.isin("DOT")).where(priceFilter | descripFilter).show(1)

DOTCodeFilter = col("StockCode") == "DOT"
priceFilter = col("UnitPrice") > 600
descripFilter = instr(col("Description"), "POSTAGE") >= 1
df.withColumn("isExpensive", DOTCodeFilter & (priceFilter | descripFilter))\
    .where("isExpensive")\
    .select("unitPrice", "isExpensive").show(5)


df.withColumn("isExpensive", expr("NOT UnitPrice <= 250"))\
    .where("isExpensive")\
    .select("Description", "UnitPrice")\
    .show(20)








