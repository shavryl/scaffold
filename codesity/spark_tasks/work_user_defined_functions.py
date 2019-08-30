from pyspark.context import SparkContext
from pyspark.sql.session import SparkSession
from pyspark.sql.functions import (
    udf, col
)
from pyspark.sql.types import IntegerType, DoubleType


sc = SparkContext('local')
spark = SparkSession(sc)


udfExampleDF = spark.range(50).toDF("num")
def power3(double_value):
    # float corresponds double
    return float(double_value ** 3)

power3(2.0)

# register our function as udf
power3udf = udf(power3)

#usage example
udfExampleDF.select(power3udf(col("num")))

# register udf as sql function
spark.udf.register("power3py", power3, DoubleType())

udfExampleDF.selectExpr("power3py(num)").show(50)
