from pyspark.context import SparkContext
from pyspark.sql.session import SparkSession
from functools import reduce


sc = SparkContext('local')
spark = SparkSession(sc)


spark.read\
    .option("header", "true")\
    .csv("data/online-data-retail-dataset.csv")\
    .repartition(2)\
    .selectExpr("instr(Description, 'GLASS') >= 1 as is_glass")\
    .groupBy('is_glass')\
    .count()\
    .collect()
