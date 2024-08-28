FROM hadoop-base:3.3.6

# Définir les variables d'environnement pour Spark
ENV SPARK_VERSION=3.4.1
ENV HADOOP_VERSION=3
ENV SPARK_HOME=/opt/spark

# Téléchargez et installez Spark
RUN mkdir -p /opt && \
    curl -o /opt/spark.tgz https://archive.apache.org/dist/spark/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz && \
    echo "Téléchargement terminé." && \
    tar -xzf /opt/spark.tgz -C /opt && \
    mv /opt/spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION} /opt/spark && \
    rm /opt/spark.tgz && \
    echo "Installation de Spark terminée."

# Télécharger les fichiers JAR pour MongoDB
RUN wget https://repo1.maven.org/maven2/org/mongodb/mongo-hadoop/mongo-hadoop-core/2.0.2/mongo-hadoop-core-2.0.2.jar -P $SPARK_HOME/jars/ && \
    wget https://repo1.maven.org/maven2/org/mongodb/mongo-hadoop/mongo-hadoop-spark/2.0.2/mongo-hadoop-spark-2.0.2.jar -P $SPARK_HOME/jars/ && \
    echo "Téléchargement des fichiers JAR pour MongoDB terminé."

# Définir les variables d'environnement
ENV PATH="$SPARK_HOME/bin:$SPARK_HOME/sbin:$PATH"

# Ajouter le script de démarrage
ADD run.sh /run.sh
RUN chmod a+x /run.sh

EXPOSE 7077 8080 4040

CMD ["/run.sh"]
