from pyspark.sql import SparkSession
from pymongo import MongoClient
import pandas as pd

# Création de la session Spark
spark = SparkSession.builder \
    .appName("MongoDB_Spark_Job") \
    .master("spark://spark:7077") \
    .getOrCreate()

# Connexion à MongoDB avec pymongo
client = MongoClient("mongodb://mongodb:27017/")
db = client['article']
collection = db['produits']

# Lire les données depuis MongoDB
data = list(collection.find())

# Convertir ObjectId en chaînes de caractères
for record in data:
    if '_id' in record:
        record['_id'] = str(record['_id'])

# Convertir en DataFrame pandas
df_pandas = pd.DataFrame(data)

# Créer DataFrame Spark
df_spark = spark.createDataFrame(df_pandas)

# Afficher les données lues depuis MongoDB
df_spark.show(truncate=False)

# Supposons que vous avez un nouveau DataFrame pandas avec les nouvelles données à insérer
# Exemple de création de nouvelles données
new_data = pd.DataFrame({
    'column1': ['value1', 'value2'],
    'column2': [10, 20]
})

# Convertir le DataFrame pandas en dictionnaires
data_to_insert = new_data.to_dict(orient='records')

# Insérer les nouvelles données dans MongoDB
collection.insert_many(data_to_insert)

# Vérifier l'insertion en lisant à nouveau les données
data_after_insertion = list(collection.find())

# Convertir ObjectId en chaînes de caractères
for record in data_after_insertion:
    if '_id' in record:
        record['_id'] = str(record['_id'])

# Convertir en DataFrame pandas
df_after_insertion = pd.DataFrame(data_after_insertion)

# Créer DataFrame Spark
df_spark_after_insertion = spark.createDataFrame(df_after_insertion)

# Afficher les données après insertion
df_spark_after_insertion.show(truncate=False)

# Arrêter la session Spark
spark.stop()
