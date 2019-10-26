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

df.groupBy("InvoiceNo", "CustomerId").count()

df.groupBy("InvoiceNo").agg(
    count("Quantity").alias("quan"),
    expr("count(Quantity)"))

df.groupBy("InvoiceNo").agg(expr("avg(Quantity)"),expr("stddev_pop(Quantity)"))

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


dfWithDate.where("CustomerId IS NOT NULL").orderBy("CustomerId")\
    .select(
        col("CustomerId"),
        col("date"),
        col("Quantity"),
        purchaseRank.alias("quantityRank"),
        purchaseDenseRank.alias("quantityDenseRank"),
        maxPurchaseQuantity.alias("maxPurchaseQuantity"))


dfNoNull = dfWithDate.drop()
dfNoNull.createOrReplaceTempView("dfNoNull")


# rollup that creates DF that includes the grand total over all dates
# the grand total for each date in the DF and the subtotal for each
# country on each date in the DF
rolledUpDF = dfNoNull.rollup("Date", "Country").agg(sum("Quantity"))\
    .selectExpr("Date", "Country", "`sum(Quantity)` as total_quantity")\
    .orderBy("Date")


cubedDF = dfNoNull.cube("Date", "Country").agg(sum(col("Quantity")))\
    .select("Date", "Country", "sum(Quantity)")\
    .orderBy("Date")

cubedDF.filter((col("Country") == "France") & (col("Date") >= "2010-12-01"))

# this DF will now have a column for every combination of country
# numeric variable and a column specifying the date.
pivoted = dfWithDate.groupBy("date").pivot("Country").sum()

pivoted.where("date > '2011-12-05'").select("date", "`USA_sum(CAST(Quantity AS BIGINT))`").show()
