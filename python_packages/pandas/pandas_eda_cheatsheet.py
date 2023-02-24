import pandas as pd
"""Pandas Exploratory Data Analysis Cheatsheet"""

"""
1. Enter File Paths:
"""
file1_csv_path ='/home/ra-terminal/datasets/job_app_data/DOB_Job_Application_Filings_csv.csv'
file2_excel_path = '/home/ra-terminal/datasets/job_app_data/DOB_Job_Application_Filings_excel.xlsx' 

"""
2. Reading Data
"""

"""Reading CSVs"""
data_csv_df = pd.read_csv(file1_csv_path, nrows=500)
# print(data_csv.shape)

"""Reading Excels"""
data_excel_df = pd.read_excel(file2_excel_path,  sheet_name='DOB_Job_Application_Filings_1', nrows=500)
data_excel2_df = pd.read_excel(file2_excel_path, sheet_name='DOB_Job_Application_Filings_2', nrows=500)
# print(data_excel_df.shape)
# print(data_excel2_df.shape)

"""3. .shape"""
print(data_csv_df)

"""4. Get Column Names""" 
# print(data_csv_df.columns) 

"""5. Get Column Count"""
# print(data_csv_df.shape[1])

"""6. Get Row Count"""
# print(data_csv_df.shape[0])

"""7. Get Column/Row Count"""
# print(data_csv_df.shape)

"""8. Get Number of Filled Cells"""
# print(data_csv_df.size)

"""9. Get File Size"""
import os
# print(os.path.getsize(file1_csv_path))

"""10. Count Number of Null Values"""
# print(data_csv_df.isna().sum().sum())

"""11. .describe()"""

"""12. Unique Values"""

"""13. .head()"""
# print(data_csv_df.head())
# print(data_csv_df.head(10))

"""14. .tail()"""
# print(data_csv_df.head(20))


"""15. .columns"""
# print(data_csv_df.columns)

"""16. df.info()"""
# print(data_csv_df.info)

"""17. Count for Distinct Values in Column"""
# print(data_csv_df['Borough'].value_counts())

"""18. Count Distinct Column Values"""
# data_csv_df['Borough'].value_counts()

"""19. Breakdown by % of Distinct Values in a Column"""
# data_csv_df['Borough'].value_counts(normalize=True)

"""20. Sort Dataframe by Column(s)"""
# print(data_csv_df.sort_values(by=['Borough'], ascending=[True]))

# print(data_csv_df.sort_values(by=['Borough','Job #'], descending=[True,False]))

"""21. Mean returns the Avg Observation For a Given Column"""
# print(data_csv_df['Borough'].mean()) #check

# print(data_csv_df[data_csv_df['Borough'] > 5].mean())
