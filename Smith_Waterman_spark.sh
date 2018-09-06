#/bash
./sbin/start-master.sh
./sbin/start-slaves.sh spark://127.0.1.1:7077
./bin/spark-submit --master spark://127.0.1.1:7077 SWSpark.py


