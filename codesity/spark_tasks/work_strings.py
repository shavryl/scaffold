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


# capitalise word first letter after a space
df.select(initcap(col("Description"))).show()

# variants of strings cast
df.select(col("Description"),
          lower(col("Description")),
          upper(lower(col("Description")))).show(2)

# adding or removing spaces
df.select(
    ltrim(lit("    HELLO    ")).alias("ltrim"),
    rtrim(lit("    HELLO    ")).alias("rtrim"),
    trim(lit("    HELLO    ")).alias("trim"),
    lpad(lit("HELLO"), 3, " ").alias("lp"),
    rpad(lit("HELLO"), 10, " ").alias("rp")).show(2)

# replace sting words
regex_string = "BLACK|WHITE|RED|GREEN|BLUE"
df.select(
    regexp_replace(col("Description"), regex_string, "COLOR").alias("color_clean"),
    col("Description")).show(2, False)

# replace characters
df.select(translate(col("Description"), "LEET", "1337"), col("Description")).show(2, False)

# extraction of string
extract_str = "(BLACK|WHITE|RED|GREEN|BLUE)"
df.select(
    regexp_extract(col("Description"), extract_str, 1).alias("color_clean"),
    col("Description")).show(2, False)

# check for string existence
containsBlack = instr(col("Description"), "BLACK") >= 1
containsWhite = instr(col("Description"), "WHITE") >= 1
df.withColumn("hasSimpleColor", containsBlack | containsWhite)\
    .where("hasSimpleColor")\
    .select("Description").show(2, False)

# location of strings
simpleColors = ["black", "white", "red", "green", "blue"]


def color_locator(column, color_string):
    return locate(color_string.upper(), column)\
        .cast("boolean")\
        .alias("is_" + c)

selectedColumns = [color_locator(df.Description, c) for c in simpleColors]
selectedColumns.append(expr("*"))

df.select(*selectedColumns).where(expr("is_white OR is_red"))\
    .select("Description").show(20, False)










