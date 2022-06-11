from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('SimpleSparkProject').getOrCreate()

df = spark.read.format("csv").load('dataset.csv')
row = df.count()
print(f'Number of Rows are: {row}')
