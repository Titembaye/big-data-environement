from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("SimpleApp").getOrCreate()

data = [("James", "Sales", 3000), ("Michael", "Sales", 4600)]
df = spark.createDataFrame(data, ["Employee Name", "Department", "Salary"])

df.show()
spark.stop()
