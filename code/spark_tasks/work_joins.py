from pyspark.sql.types import StructField, StructType, StringType, LongType
from pyspark.context import SparkContext
from pyspark.sql.session import SparkSession
from pyspark.sql.functions import *
from pyspark.sql import Row


sc = SparkContext('local')
spark = SparkSession(sc)

person = spark.createDataFrame([
    (0, "Bill Chambers", 0, [100]),
    (1, "Matei Zaharia", 1, [500, 250, 100]),
    (2, "Michael Armbrust", 1, [250, 100])])\
    .toDF("id", "name", "graduate_program", "spark_status")

graduateProgram = spark.createDataFrame([
    (0, "Masters", "School of Information", "UC Berkeley"),
    (2, "Masters", "EECS", "UC Berkeley"),
    (1, "Ph.D.", "EECS", "UC Berkeley")])\
    .toDF("id", "degree", "department", "school")

sparkStatus = spark.createDataFrame([
    (500, "Vice President"),
    (250, "PMC Member"),
    (100, "Contributor")])\
    .toDF("id", "status")

# register datasets as tables
person.createOrReplaceTempView("person")
graduateProgram.createOrReplaceTempView("graduateProgram")
sparkStatus.createOrReplaceTempView("sparkStatus")

# inner joins evalueate the keys in both DFs or tables and include
# and join together only the rows that evaluate to true
joinExpression = person["graduate_program"] == graduateProgram['id']

# inner joins are the default join so we just need to specify our
# left DF and join the right in the JOIN expression
person.join(graduateProgram, joinExpression)

# or specify this explicitly by passing third parameter, the joinType:
joinType = 'inner'
person.join(graduateProgram, joinExpression, joinType).show()
