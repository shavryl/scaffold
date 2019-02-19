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
df.createOrReplaceTempView("dfTable")


fabricatedQuantity = pow(col("Quantity") * col("UnitPrice"), 2) + 5
df.select(expr("CustomerId"), fabricatedQuantity.alias("realQuantity")).show(2)

df.selectExpr(
    "CustomerId",
    "(POWER((Quantity * UnitPrice), 2.0) + 5) as realQuantity")\
    .show(2)

df.select(round(lit("2.5")), bround(lit("2.5"))).show(2)

df.stat.corr("Quantity", "UnitPrice")
df.select(corr("Quantity", "UnitPrice")).show()

df.describe().show()

colName = "UnitPrice"
quantileProbs = [0.5]
relError = 0.05
df.stat.approxQuantile("UnitPrice", quantileProbs, relError)
df.stat.crosstab("StockCode", "Quantity").show(1)

df.stat.freqItems(["StockCode", "Quantity"]).show()

# add unique ID to each row
df.select(monotonically_increasing_id()).show(2)
