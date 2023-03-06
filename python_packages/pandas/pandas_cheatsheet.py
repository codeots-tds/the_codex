import pandas as pd

"""Dataframe Manipulation with Pandas Cheatsheet"""

"""
Enter File Paths:
"""
file1_csv_path ='/home/ra-terminal/datasets/mass_public_schools/MA_Public_Schools_2017.csv'
file2_excel_path = '/home/ra-terminal/datasets/mass_public_schools/MA_Public_Schools_2017_excel.xlsx' 

"""
Reading Data with Column Subset
"""
cols = ['School Code',	'School Name',	'School Type',	'Function',	'Contact Name', 'Address 1', 'Address 2', 'Town', 'State', 'Zip', 'Phone',	'Fax', 'Grade', 'District Name', 'District Code',	
        'PK_Enrollment', 'K_Enrollment', '1_Enrollment', '2_Enrollment', '3_Enrollment',	
        '4_Enrollment',	'5_Enrollment',	 '6_Enrollment',	
        '7_Enrollment',	'8_Enrollment',	'9_Enrollment',	'10_Enrollment', '11_Enrollment',	
        '12_Enrollment',	'SP_Enrollment','TOTAL_Enrollment']
"""Reading CSVs"""
# data_csv_df = pd.read_csv(file1_csv_path, nrows=500)
# print(len(data_csv_df.columns))
data_csv_df = pd.read_csv(file1_csv_path, nrows=500, usecols=cols)
# print(len(data_csv_df.columns))

"""Reading Excels"""
# data_excel_df = pd.read_excel(file2_excel_path,  
#                               sheet_name='MA_Public_Schools_2017_1', nrows=500, usecols=cols)
# data_excel2_df = pd.read_excel(file2_excel_path, 
#                                sheet_name='MA_Public_Schools_2017_2', nrows=500)
# print(data_excel_df.head(5))
# print(data_excel2_df.head(5))

"""index - col"""
# data_csv_df2 = pd.read_csv(file1_csv_path, nrows=500, index_col=1)
# print(data_csv_df2.head(5))

"""Loc - Location
"""
loc_val1 = data_csv_df.loc[3, 'Zip']
"""variable = dataframe.loc[row number, column name]"""
# print(loc_val1)

loc_val2 = data_csv_df.loc[3, 'Zip'] = 6783
"""variable = dataframe.loc[row number, column name]"""
# print(loc_val2)

loc_val3 = data_csv_df.loc[3:10, 'Contact Name':'Fax']
"""variable = dataframe.loc[row start:row end, column start:column end]"""
# print(loc_val3.columns)

"""
iLoc - Index Location
"""
# iloc_val1 = data_csv_df.iloc[3:10, 0:5]
"""variable = df.iloc[row_start:row_end, column_start:column_end]"""
# print(iloc_val1)

# iloc_val2 = data_csv_df.iloc[3:10:2, 0:10:2]
"""variable = df.iloc[row_start:row_end:step, column_start:column_end:step]"""
# print(iloc_val2)

"""
iat - Index At
"""
# iat_val1 = data_csv_df.iat[5, 2]
"""variable = df.iat[row number, column number]"""
# print(iat_val1)


"""at - At
"""
# at_val1 = data_csv_df.at[5, 'School Type']
"""variable = df.at[row number, column name]"""
# print(at_val1)

""" recheck this ---------------------
set index - setting start index after loading df
"""
set_idx_data_csv_df = data_csv_df.set_index('Contact Name', inplace = True)
"""variable = df.set_index(column name, inplace=True)"""
# print(set_idx_data_csv_df.columns)


"""Creating a Subset of a Dataframe"""
subset_data_df = data_csv_df[['Address 1',	'Address 2', 'Town', 'State', 
                              'Zip', 'Phone', 'Fax']]
"""variable = df[['column 1', 'column 2', 'column 5', 'column 9']]"""
# print(subset_data_df.head(5))

"""Iterating through dataframes using .iterrows()"""
# for idx, row in data_csv_df.iterrows():
#     school_name = row['School Name']
#     school_type = row['School Type']
#     function = row['Function']
#     addr1 = row['Address 1']

#     print(f'''School Name:, {school_name}, School Type:, {school_type}, 
#           Function:, {function}, Address:, {addr1}''')
#     print('-------------------------------')

"""Convert Pandas Column or Series to Another Datatype"""
# print(type(data_csv_df['7_Enrollment'][0]))
# data_csv_df['7_Enrollment'] = data_csv_df['7_Enrollment'].astype(str)
# print(type(data_csv_df['7_Enrollment'][0]))

"""Not Operator"""
# data_block3 = data_csv_df[~data_csv_df['Town'].str.contains('Auburn')]
# print(data_block3['Town'] == 'Auburn')

"""Insert"""
print(data_csv_df.loc[4, 'Phone'])
# data_csv_df.insert(4, 'Phone', '718-254-9369')
# """dataframe.insert(loc, column, value, allow_duplicates = False)"""
# print(data_csv_df.loc[4, 'Phone'])

"""17. Create New Column"""
# data_csv_df['New_Col'] = None
# """df['column name'] = value"""

"""18. Drop Duplicates"""
# print(data_csv_df.shape[0])
# data_csv_df.drop_duplicates(keep = 'first', inplace=True)
# data_csv_df_not_inplace = data_csv_df.drop_duplicates(keep = 'first')
# print(data_csv_df.shape[0])


"""19. Drop Column(s)"""
# data_csv_df.drop('column name', axis=1, inplace=True)
# print(data_csv_df.columns)
# data_csv_df_coldrop_not_inplace = data_csv_df.drop(columns=['House #', 'Job Status']
# , axis=1)
# print(data_csv_df_coldrop_not_inplace.columns)

"""20. .where """
