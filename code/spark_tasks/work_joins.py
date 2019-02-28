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
person.join(graduateProgram, joinExpression, joinType)

# outer joins evaluate the keys in both of the DF or tables and includes
# and joins together the rows that evaluate to true or false, if there
# is no equivalent row in either the left or right DF, spark will insert null:
joinType = 'outer'
person.join(graduateProgram, joinExpression, joinType)

# left outer joins evaluate the keys in both of the DF or tables and
# includes all rows from the left DF as well as any rows in the right DF
# that have a match in the left DF. If there is no equivalent row in
# the right DF spark will insert null:
joinType = 'left_outer'
graduateProgram.join(person, joinExpression, joinType)

# right outer joins evaluate the keys in both of the DF and includes
# all rows from the right DF as well as any rows in the left DF that have a
# match in the right DF. If there is no equivalent spark will insert null
joinType = 'right_outer'
person.join(graduateProgram, joinExpression, joinType)

# semi joins do not actually include any values from the right DF.
# they only compare values to see if the value exists in the second DF.
# if the value does exist, those rows will be kept in the result, even
# if there are duplicate keys in the left DF. Think of left semi joins
# as filters on a DF as opposed to the function of a conventional join:
joinType = 'left_semi'
graduateProgram.join(person, joinExpression, joinType)

gradProgram2 = graduateProgram.union(spark.createDataFrame([
    (0, "Masters", "Duplicated Row", "Duplicated School")]))
gradProgram2.createOrReplaceTempView("gradProgram2")

gradProgram2.join(person, joinExpression, joinType)

# left anti joins are the opposite of left semi joins. Like left semi joins, they
# do not actually include any values from the right DF. They only compare values
# to see if the value exists in the second DF. However, rather than keeping the
# values that exist in the second DF they keep only the values that do not have a
# corresponding key in the second DF. Think of anti joins as a NOT IN sql style filter
joinType = 'left_anti'
graduateProgram.join(person, joinExpression, joinType)

# cross join in simplest terms are inner joins that do not specify a predicate.
# Cross joins will join every single row in the left DF to ever single row in the
# right DF. This will cause an absolute explosion in the number of rows contained
# in the resulting DF.
joinType = 'cross'
graduateProgram.join(person, joinExpression, joinType).show()

person.crossJoin(graduateProgram).show()











