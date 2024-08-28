# Dockerfile pour Spark Worker
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

# Définir les variables d'environnement
ENV PATH="$SPARK_HOME/bin:$SPARK_HOME/sbin:$PATH"

# Ajouter le script de démarrage
ADD run.sh /run.sh
RUN chmod a+x /run.sh

EXPOSE 7077 8080 4040

CMD ["/run.sh"]
