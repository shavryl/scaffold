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
    .load("data/online-data-retail-dataset.csv")\
    .coalesce(5)
df.cache()
df.createOrReplaceTempView("dfTable")


df.select(
    count("Quantity").alias("total_transactions"),
    sum("Quantity").alias("total_purchases"),
    avg("Quantity").alias("avg_purchases"),
    expr("mean(Quantity)").alias("mean_purchases"))\
    .selectExpr(
    "total_purchases/total_transactions",
    "avg_purchases",
    "mean_purchases").show()

df.select(var_pop("Quantity"), var_samp("Quantity"),
          stddev_pop("Quantity"), stddev_samp("Quantity")).show()

df.select(skewness("Quantity"), kurtosis("Quantity")).show()

# correlation and covariance
df.select(corr("InvoiceNo", "Quantity"), covar_samp("InvoiceNo", "Quantity"),
          covar_pop("InvoiceNo", "Quantity")).show()

# collect variants before aggregation
df.agg(collect_set("Country"), collect_list("Country")).show(1)










