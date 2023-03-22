from pyspark.sql import SparkSession, SQLContext
import pyspark.pandas as psp

import os
os.environ["PYARROW_IGNORE_TIMEZONE"] = "1"

pyspark = SparkSession.builder \
            .appName("Pyspark_Pandas_Test") \
            .master("local") \
            .config('spark.ui.port', '4040') \
            .getOrCreate()
print(pyspark)

path1 = '/home/ra-terminal/datasets/covid/archive_extracted/cord_19_embeddings/cord_19_embeddings_2022-06-02.csv'


df1 = psp.read_csv(path1)
print(type(df1))

input('Press enter to exit:')
pyspark.stop()

if __name__ == "__main__":
    pass