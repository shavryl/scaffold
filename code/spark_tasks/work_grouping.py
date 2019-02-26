from pyspark.sql.types import StructField, StructType, StringType, LongType
from pyspark.context import SparkContext
from pyspark.sql.session import SparkSession
from pyspark.sql.functions import *
from pyspark.sql import Row
from pyspark.sql.window import Window


sc = SparkContext('local')
spark = SparkSession(sc)

df = spark.read.format("csv")\
    .option("header", "true")\
    .option("inferSchema", "true")\
    .load("data/online-data-retail-dataset.csv")\
    .coalesce(5)
df.cache()
df.createOrReplaceTempView("dfTable")

df.groupBy("InvoiceNo", "CustomerId").count().show()

df.groupBy("InvoiceNo").agg(
    count("Quantity").alias("quan"),
    expr("count(Quantity)")).show()

df.groupBy("InvoiceNo").agg(expr("avg(Quantity)"),expr("stddev_pop(Quantity)")).show()

# add date column and convert invoice date into a column with date information
dfWithDate = df.withColumn("date", to_date(col("InvoiceDate"), "MM/d/yyyy H:mm"))
dfWithDate.createOrReplaceTempView("dfWithDate")

# create window specification. The ordering determines the ordering
# within a given partition, and the frame specification (rowsBetween)
# states which rows will be included in the frame based on its
# reference to the current input row.
windowSpec = Window\
    .partitionBy("CustomerId", "date")\
    .orderBy(desc("Quantity"))\
    .rowsBetween(Window.unboundedPreceding, Window.currentRow)


# use agg function to learn more about each specific customer
# example establishing the maximum purchase quantity over all time
# we indicate the window specification that defines to which
# frames of data this function will apply
maxPurchaseQuantity = max(col("Quantity")).over(windowSpec)


# we can now use this in a DF select statement
# before we will create the purchase quantity rank
# we use the dense_rank function to determine which date
# had the maximum purchase quantity for every customer
purchaseDenseRank = dense_rank().over(windowSpec)
purchaseRank = rank().over(windowSpec)











