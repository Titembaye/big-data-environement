FROM hadoop-base:3.3.6

ENV PIG_VERSION 0.17.0
ENV PIG_HOME /opt/pig

# Installer wget et curl, télécharger et installer Pig
RUN apt-get update && \
    apt-get install -y wget curl && \
    wget https://archive.apache.org/dist/pig/pig-$PIG_VERSION/pig-$PIG_VERSION.tar.gz && \
    tar -xzf pig-$PIG_VERSION.tar.gz && \
    mv pig-$PIG_VERSION $PIG_HOME && \
    ln -s $PIG_HOME/bin/pig /usr/bin/pig && \
    rm pig-$PIG_VERSION.tar.gz

# Télécharger les fichiers JAR nécessaires pour la connexion avec MongoDB
RUN wget https://repo1.maven.org/maven2/org/mongodb/mongo-hadoop/mongo-hadoop-core/2.0.2/mongo-hadoop-core-2.0.2.jar -P $PIG_HOME/lib/ && \
    wget https://repo1.maven.org/maven2/org/mongodb/mongo-hadoop/mongo-hadoop-pig/2.0.2/mongo-hadoop-pig-2.0.2.jar -P $PIG_HOME/lib/ && \
    echo "Téléchargement des fichiers JAR pour MongoDB terminé."

EXPOSE 8080

CMD ["pig"]
