import pyspark
from pyspark.sql.functions import *
from pyspark.sql import SparkSession
from delta import *
from delta.tables import DeltaTable

builder = pyspark.sql.SparkSession.builder.appName("MyApp") \
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
    .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog") \
    .config("spark.sql.session.timeZone", "America/Sao_Paulo") \
    .config("spark.sql.files.maxRecordsPerFile", 100000)

spark = configure_spark_with_delta_pip(builder) \
        .config("spark.executor.memory", "4g") \
        .config("spark.driver.memory", "4g") \
        .config("spark.memory.fraction", "0.8") \
        .config("spark.sql.shuffle.partitions", "200") \
        .config("spark.sql.debug.maxToStringFields", 1000).getOrCreate()


df = spark.read.csv("file/postings.csv", header=True)

df.write.format("delta").mode("overwrite").save('raw/jobs')