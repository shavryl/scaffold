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
words.flatMap(lambda word: list(word)).take(5)

# to sort an RDD you must use the sortBy method and just like any
# other RDD operation you do this by specifying a function to extract
# a value from the objects in your RDDs and then sort based on that.
words.sortBy(lambda word: len(word) * -1).take(2)

spark.sparkContext.parallelize(range(1, 21)).reduce(lambda x, y: x + y)

def wordLengthReducer(leftWord, rightWord):
    if len(leftWord) > len(rightWord):
        return leftWord
    else:
        return rightWord

words.reduce(wordLengthReducer)

words.map(lambda word: (word.lower(), 1))
keyword = words.keyBy(lambda word: word.lower()[0])

keyword.mapValues(lambda word: word.upper()).collect()
keyword.flatMapValues(lambda word: word.upper()).collect()

keyword.keys().collect()
keyword.values().collect()
keyword.lookup('s')


chars = words.flatMap(lambda word: word.lower())
KVcharacters = chars.map(lambda letter: (letter, 1))
def maxFunc(left, right):
    return max(left, right)

def addFunc(left, right):
    return left + right

nums = sc.parallelize(range(1, 31), 5)









print(ttr)







