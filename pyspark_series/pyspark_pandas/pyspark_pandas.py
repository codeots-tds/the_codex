import os
os.environ["PYARROW_IGNORE_TIMEZONE"] = "1"

import pyspark
from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum, avg, max
import pyspark.pandas as pspd
import pandas as pd


class Pd_Pyspark_Class:
    def __init__(self, **kwargs):
        self.spark = kwargs.get('spark')
        self.path = kwargs.get('path')
        self.sc = kwargs.get('sc')
        self.psdf = pspd.read_csv(self.path, nrows=10000)

if __name__ == "__main__":
    spark = SparkSession \
        .builder \
        .appName("process_labor_data") \
        .config("config option", "config value") \
        .getOrCreate()
    sc = pyspark.SparkContext.getOrCreate()
    print(spark,'---',sc)
    path = '/home/ra-terminal/datasets/job_app_data/DOB_Job_Application_Filings.csv'
    DOB_job_obj = Pd_Pyspark_Class(spark = spark, path = path, sc = sc)
    print(DOB_job_obj.psdf.head(5))
    print(type(DOB_job_obj.psdf))