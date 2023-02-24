import pandas as pd

"""Dataframe Manipulation with Pandas Cheatsheet"""

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

"""3. index - col"""
data_csv_df2 = pd.read_csv(file1_csv_path, nrows=500, index_col=1)
# print(data_csv_df2.shape)

"""4. Loc - Location
"""
loc_val1 = data_csv_df.loc[3, 'Job Status Descrp']
"""variable = dataframe.loc[row number, column name]"""

loc_val2 = data_csv_df.loc[3:10, 'Lot':'Job Status Descrp']
"""variable = dataframe.loc[row start:row end, column start:column end]"""
# print(loc_val1)
# print(loc_val2)

"""
5. iLoc - Index Location
"""
iloc_val1 = data_csv_df.iloc[3:20, 0:5]
"""variable = df.iloc[row_start:row_end, column_start:column_end]"""

iloc_val2 = data_csv_df.iloc[3:20:2, 0:10:2]
"""variable = df.iloc[row_start:row_end:step, column_start:column_end:step]"""
# print(iloc_val1)
# print(iloc_val2)

"""
6. iat - Index At
"""
iat_val1 = data_csv_df.iat[5, 2]
"""variable = df.iat[row number, column number]"""
# print(iat_val1)


"""7. at - At
"""
at_val1 = data_csv_df.at[10, 'Borough']
"""variable = df.at[row number, column name]"""

"""
8. set index - setting start index after loading df
"""
set_idx_data_csv_df = data_csv_df.set_index('Borough', inplace = True)
"""variable = df.set_index(column name, inplace=True)"""
# print(set_idx_data_csv_df.shape)


"""9. Creating a Subset of a Dataframe"""
subset_data_df = data_csv_df[['House #',	'Street Name',	'Block', 'Lot',	'Bin #']]
"""variable = df[['column 1', 'column 2', 'column 5', 'column 9']]"""
print(subset_data_df.shape)

"""13. Iterating through dataframes using .iterrows()"""
# for idx, row in data_csv_df.iterrows():
#     print(idx, '>>>>')

"""14. Convert Pandas Column or Series to Another Datatype"""
print(type(data_csv_df['Block'][0]))
data_csv_df['Block'] = data_csv_df['Block'].astype(str)
print(type(data_csv_df['Block'][0]))

"""15. Not Operator"""
data_block3 = data_csv_df[~data_csv_df['Job Status'].str.contains('R')]
# print(data_block3)

"""16.  Insert"""
# data_csv_df.insert(4, 'House #')
"""dataframe.insert(loc, column, value, allow_duplicates = False)"""

"""17. Create New Column"""
data_csv_df['New_Col'] = None
"""df['column name'] = value"""

"""18. Drop Duplicates"""
print(data_csv_df.shape[0])
data_csv_df.drop_duplicates(keep = 'first', inplace=True)
data_csv_df_not_inplace = data_csv_df.drop_duplicates(keep = 'first')
print(data_csv_df.shape[0])


"""19. Drop Column(s)"""
data_csv_df.drop('column name', axis=1, inplace=True)
print(data_csv_df.columns)
data_csv_df_coldrop_not_inplace = data_csv_df.drop(columns=['House #', 'Job Status']
, axis=1)
print(data_csv_df_coldrop_not_inplace.columns)