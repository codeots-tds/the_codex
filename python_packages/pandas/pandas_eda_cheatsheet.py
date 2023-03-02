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
# print(data_csv_df.shape)

"""Reading Excels"""
data_excel_df = pd.read_excel(file2_excel_path,  
                              sheet_name='DOB_Job_Application_Filings_1', nrows=500)
data_excel2_df = pd.read_excel(file2_excel_path, 
                               sheet_name='DOB_Job_Application_Filings_2', nrows=500)
# print('excel 1:', data_excel_df.shape)
# print('excel 2:', data_excel2_df.shape)

"""3. .shape"""
# print(data_csv_df.shape)

"""4. Get Column Count"""
# print(data_csv_df.shape[1])

"""5. Get Row Count"""
# print(data_csv_df.shape[0])

"""6. Get Column Names""" 
# print(data_csv_df.columns) 

"""7. Get Number of Filled Cells"""
# print(data_csv_df.size)

"""8. Get File Size"""
import os
# print(os.path.getsize(file1_csv_path))

"""9. Count Number of Null Values"""
# print(data_csv_df.isna().sum().sum())

"""10. .describe()"""
# print(data_csv_df['Borough'].describe())
# print(data_csv_df.describe())

"""11. Unique Values"""
# print(data_csv_df['Borough'].unique())


"""12. .head()"""
# print(data_csv_df.head(10))

"""13. .tail()"""
# print(data_csv_df.tail(5))

"""14. .columns"""
# print(data_csv_df.columns)

"""15. df.info()"""
# print(data_csv_df.info())

"""16. Count Distinct Column Values"""
# print(data_csv_df['Borough'].value_counts())

"""17. Breakdown by % of Distinct Values in a Column"""
# print(data_csv_df['Borough'].value_counts(normalize=True) * 100)

"""18. Sort Dataframe by Column(s)"""
# print(data_csv_df.sort_values(by=['Borough'], ascending=[True]))
# print(data_csv_df.sort_values(by=['Borough','Job #'], ascending=[True,False]))

"""19. Mean returns the Average Observation"""
# print(data_csv_df.mean()) 
# print(data_csv_df[data_csv_df['Borough'].mean() > 2])

"""20. Returns the Median Observation of a Given Series"""
# print(data_csv_df.median(axis = 1))
# print(data_csv_df['Block'].median(axis = 0, skipna = True, level = None, numeric_only=True))

"""21. Returns the Mode Observation of a Given Series"""
# print(data_csv_df['Block'].mode())

"""22. Standard Deviation"""
# print(data_csv_df.std())
print(data_csv_df['Block'].std())