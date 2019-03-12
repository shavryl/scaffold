from pyspark.context import SparkContext
from pyspark.sql.session import SparkSession
from functools import reduce


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

KVcharacters.countByKey()

KVcharacters.groupByKey().map(lambda row: (row[0], reduce(addFunc, row[1]))).collect()

KVcharacters.reduceByKey(addFunc).collect()

# requires a null and start value and then requires you to specify
# two different functions. The first aggregates within partitions
# the second aggregates across partitions
nums.aggregate(0, maxFunc, addFunc)

# does the same as aggregate but does so in a different way. It basically
# 'pushes down' some of the subaggregations (creating a tree from executor
# to executor) before performing the final aggregation on the driver
depth = 3
nums.treeAggregate(0, maxFunc, addFunc, depth)

# same as aggregate but instead doing it partition by partition
# it does it by key, follows the same properties
KVcharacters.aggregateByKey(0, addFunc, maxFunc).collect()

# this combiner operates on a given key and merges the values according to
# some function. It then goes to merge the different outputs of the combiners
# to give us result. We can specify the number of output partitions
def valToCombiner(value):
    return [value]

def mergeValuesFunc(vals, valToAppend):
    vals.append(valToAppend)
    return vals

def mergeCombinerFunc(vals1, vals2):
    return vals1 + vals2

outputPartitions = 6
KVcharacters.combineByKey(
    valToCombiner,
    mergeValuesFunc,
    mergeCombinerFunc,
    outputPartitions
).collect()


# CoGroups give you the ability to group together two key-value RDDS
# this joins the given values by key. THis is effectively just a group-based
# join on an RDD. When doing this, you can also specify a number of output
# partitions or a custom partitioning function to control exactly how this
# data is distributed across the cluster
import random
distinctChars = words.flatMap(lambda word: word.lower()).distinct()
charRDD = distinctChars.map(lambda c: (c, random.random()))
charRDD2 = distinctChars.map(lambda c: (c, random.random()))
charRDD.cogroup(charRDD2).take(5)

# example of inner join on RDDs
keyedChars = distinctChars.map(lambda c: (c, random.random()))
outputPartitions = 10
KVcharacters.join(keyedChars).count()
KVcharacters.join(keyedChars, outputPartitions).count()

# zip creates PairRDD. The two RDDs must have the same number of
# partitions as well as the same number of elements:
numRange = sc.parallelize(range(10), 2)
words.zip(numRange).collect()

# coalesce effectively collapses partitions on the same worker
# in order to avoid a shuffle of the data then repartitioning
words.coalesce(1).getNumPartitions()

# the repartition operation allows you to repartition your data
# up or down but performs a shuffle across nodes in the process.
# increasing the number of partitions can increase the level of
# parallelism when operating in map- and filter-type operations
words.repartition(10)

supplementalData = {"Spark": 1000, "Definitive": 200,
                    "Big": -300, "Simple": 100}

suppBroadcast = spark.sparkContext.broadcast(supplementalData)

# we will create a key-value pair according to the value we might
# have in the map. If we lack the value we will replace it with 0:
ttr = words.map(lambda word: (word, suppBroadcast.value.get(word, 0)))\
    .sortBy(lambda wordPair: wordPair[1])\
    .collect()


print(ttr)







