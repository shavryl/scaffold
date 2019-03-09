from pyspark.context import SparkContext
from pyspark.sql.session import SparkSession


sc = SparkContext('local')
spark = SparkSession(sc)

# rdd of type row
spark.range(10).toDF("id").rdd.map(lambda row: row[0])

# to create an RDD from a collection us parallelize method on a SparkContext
# this turns a single node collection into a parallel collection
myCollection = "Spark The Definitive Guide : Big Data Processing Made Simple".split(" ")
words = spark.sparkContext.parallelize(myCollection, 2)
words.setName("myWords")
words.name()


def startsWithS(individual):
    return individual.startswith("S")

words.filter(lambda word: startsWithS(word)).collect()


# you specify a function that returns the value that you want, given input
words2 = words.map(lambda word: (word, word[0], word.startswith('S')))

words2.filter(lambda record: record[2]).take(5)

# flatmap provides a simple extension of the map function
# sometimes each current row should return multiple rows instead
# for example you might want to take your set of words and flatmap
# it into a set of characters.
ttr = words.flatMap(lambda word: list(word)).take(5)




print(ttr)









