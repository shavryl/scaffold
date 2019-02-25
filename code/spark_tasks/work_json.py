from pyspark.context import SparkContext
from pyspark.sql.session import SparkSession
from pyspark.sql.functions import (
    get_json_object, json_tuple,
    col, to_json, from_json,
)
from pyspark.sql.types import *


sc = SparkContext('local')
spark = SparkSession(sc)

df = spark.read.format("csv")\
    .option("header", "true")\
    .option("inferSchema", "true")\
    .load("data/2010-12-01.csv")
df.createOrReplaceTempView("dfTable")

jsonDF = spark.range(1).selectExpr("""
    '{"myJSONKey" : {"myJSONValue" : [1, 2, 3]}}' as jsonString""")

jsonDF.select(
    get_json_object(col("jsonString"), "$.myJSONKey.myJSONValue[1]").alias("column"),
    json_tuple(col("jsonString"), "myJSONKey")).show(2, False)

# the other way
jsonDF.selectExpr(
    "json_tuple(jsonString, '$.myJSONKey.myJSONValue[1]') as column")\
    .show(2)

df.selectExpr("(InvoiceNo, Description) as myStruct")\
    .select(to_json(col("myStruct")))

# it also accepts a dict(map) of parameters that are the same
# as the JSON data source. You can use the from_json function
# to parse this (or other JSON data) back in. This naturally
# requires you to specify a schema, and optionally you can
# specify a map of options as well:
parseSchema = StructType((
    StructField("InvoiceNo", StringType(), True),
    StructField("Description", StringType(), True)))

df.selectExpr("(InvoiceNo, Description) as myStruct")\
    .select(to_json(col("myStruct")).alias("newJSON"))\
    .select(from_json(col("newJSON"), parseSchema), col("newJSON")).show(20, False)





 













