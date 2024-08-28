from pyspark.sql import SparkSession

# Créer une session Spark
"""spark = SparkSession.builder \
    .appName("MongoDBSparkConnector") \
    .config("spark.mongodb.input.uri", "mongodb://mongodb:27017/article.produits") \
    .config("spark.mongodb.output.uri", "mongodb://mongodb:27017/article.produits") \
    .config("spark.jars.packages", "org.mongodb.spark:mongo-spark-connector_2.12:10.4.0") \
    .getOrCreate() """
  

# URL de connexion MongoDB sans authentification
MONGO_URL = "mongodb://mongodb:27017/article"
COLLECTION = "produits"

# Création de la SparkSession avec la configuration MongoDB
spark = SparkSession.builder \
    .appName('MongoDBSparkConnector') \
    .config('spark.mongodb.input.uri', MONGO_URL) \
    .config('spark.mongodb.input.collection', COLLECTION) \
    .config('spark.mongodb.output.uri', MONGO_URL) \
    .getOrCreate()

# Lecture des données depuis MongoDB
df = spark.read.format("mongo").load()

# Afficher les données
df.show()

# Exemple d'écriture de données dans MongoDB
data = [("item1", 10), ("item2", 20)]
df_write = spark.createDataFrame(data, ["item", "quantity"])
df_write.write.format("mongo").mode("append").save()
