# from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession, SQLContext
import pyspark.pandas as psp
import pandas as pd

import os
os.environ["PYARROW_IGNORE_TIMEZONE"] = "1"

"""Need to knows:
-Change module prefixes from standard pandas to something else. ex. pd to psp. 
-pd.function format may not work in all cases, however 
the dataframe.method() syntax might.
"""

#---------------------------------------Previous way of configuring Spark App
"""Creating Spark Conf object"""
# pyspark_conf = SparkConf() \
#             .setAppName("myApp") \
#             .setMaster("local") \
            # .config('spark.driver.bindAddress','localhost') \
            # .config('spark.ui.port', '4050') \
            # .getOrCreate()

"""you can customize how you want pyspark to run using the conf object.
right here we're creating a pyspark app called myApp and running it in local mode"""

"""Creating Spark Context Object"""
# sc = SparkContext(conf=pyspark_conf)

"""This helps you connect to the spark cluster. Make sure to pass the spark conf object
into your spark context object"""
#---------------------------------------------------
#----------------------------------------------------

#----------------------------------------------------Start Here
"""Creating Spark Session Object"""
pyspark = SparkSession.builder \
            .appName("Pyspark_Pandas_Test") \
            .master("local") \
            .config('spark.ui.port', '4040') \
            .getOrCreate()
print(pyspark)
"""After Pyspark 3.0, Pyspark can now use the Spark Session object as the entrypoint
to the application instead of Spark Conf and Spark Context. Here you can name your application, 
setup your node configuraiton(whether local or distributed), 
the port for the ui and other parameters as well!"""


"""Using Pandas API on Pyspark"""
"""Loading Data"""
path1 = '/home/ra-terminal/datasets/covid/archive_extracted/cord_19_embeddings/cord_19_embeddings_2022-06-02.csv'

"""Standard Pandas"""
# df1 = pd.read_csv(path1, nrows = 500)
# print(df1.shape)
# print(type(df1))

"""Pyspark Pandas"""
df2 = psp.read_csv(path1)
# # print(df2.shape)
print(type(df2))


"""
nrows = number of rows.
header = to include column names in data or not. (0, 1, None)
usecols= list of which columns you'd like to include when loading data
"""

"""Row/Column Count"""
# print(df1.shape)
# print(df2.shape)

"""Get File Size"""
# print(os.path.getsize(path1))

"""Filled Number of Cells"""
# print('Filled Cells 1:', df1.size)



input('Press enter to exit:')
pyspark.stop()
if __name__ == "__main__":
    pass