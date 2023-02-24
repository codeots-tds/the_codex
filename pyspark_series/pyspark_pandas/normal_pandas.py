import pandas as pd

path2= '/home/ra-terminal/datasets/job_app_data/DOB_Job_Application_Filings.csv'
norm_pandas_df = pd.read_csv(path2, nrows=10000)
print(norm_pandas_df)
print(type(norm_pandas_df))