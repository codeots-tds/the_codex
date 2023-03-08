import pandas as pd
import numpy as np
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
# data_csv_df = pd.read_csv(file1_csv_path, nrows=1000)
# print(len(data_csv_df.columns))
data_csv_df = pd.read_csv(file1_csv_path, usecols=cols)
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
# set_idx_data_csv_df = data_csv_df.set_index('Contact Name', inplace = True)
"""variable = df.set_index(column name, inplace=True)"""
# print(set_idx_data_csv_df.columns)


"""Creating a Subset of a Dataframe"""
subset_data_df = data_csv_df[['Address 1', 'Address 2', 'Town', 'State', 
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
# data_csv_df.insert(8, 'Dataset Type', 'School Demographics')
# """dataframe.insert(loc, column, value, allow_duplicates = False)"""
# print(data_csv_df['Dataset Type'])

"""Create New Column"""
# data_csv_df['New_Col'] = None
"""df['column name'] = value"""
# print(data_csv_df['New_Col'])

"""Drop Duplicates"""
dup_list = []
# print(data_csv_df.shape, 'first df check')
dup_list.append(data_csv_df.loc[0:51, 
                        f'School Code':
                        f'TOTAL_Enrollment'])

for idx, new_row in enumerate(dup_list):
    data_csv_df2 = data_csv_df.append(new_row)

# print(data_csv_df2.shape, 'new df check')
# data_csv_df2.drop_duplicates(keep= 'first', inplace = True)
# print(data_csv_df2.shape, 'Last check after dropping duplicates.')

print('Old', data_csv_df2['School Type'].shape, data_csv_df2['Town'].shape)
sub_cols = ['School Type', 'Town']
data_csv_df2.drop_duplicates(keep ='first', subset = sub_cols, inplace = True)
print('after dropping dupes', data_csv_df2['School Type'].shape, 
       data_csv_df2['Town'].shape)

"""Drop Column(s)"""
# data_csv_df.drop(columns=['Grade', 'Phone']
# , axis=1, inplace=True)
# print(data_csv_df.columns)

""".where """
# df_public_schools = data_csv_df.where(data_csv_df['School Type']=='Public School')
# print(df_public_schools
#       [['School Code','School Type', 'School Name', 'State', 'Phone']].head(5))

# district_list = ['Agawam', 'Abington', 'Abby Kelley Foster Charter Public (District)', 
#         'Benjamin Banneker Charter Public (District)', 
#         'Phoenix Charter Academy (District)', 'Bentley Academy Charter School (District)', 
#         'Excel Academy Charter (District)']

# filter1 = data_csv_df['School Type']=='Public School'
# filter2 = data_csv_df['District Name'].isin(district_list)
# df_public_schools = data_csv_df.where(filter1 & filter2)
# print(df_public_schools
#       [['School Code','School Type', 'School Name', 'State', 'Phone']].head(20))