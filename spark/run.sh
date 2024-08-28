#!/bin/bash

# Démarrer le Spark master
$SPARK_HOME/sbin/start-master.sh

# Démarrer le Spark worker (ajoutez ici des configurations supplémentaires si nécessaire)
$SPARK_HOME/sbin/start-worker.sh spark://localhost:7077

# Conserver le conteneur en cours d'exécution
tail -f /dev/null
