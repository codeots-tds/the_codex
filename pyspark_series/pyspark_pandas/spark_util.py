import pyspark

"""
Two types of methods in spark: 
a. Transformations - map(), reduceByKey()
b. Actions - take(), reduce(), saveAsTextFile(), collect()

4 important methods:
-filter()
-map()
-reduce()
-lambda()
"""

def get_rows(df, num):
    """
    prints x number of rows like pandas df.head()
    """
    return df.take(num)

def map_function(df):
    """
    -maps function you want to apply to your chosen element(s) in the RDD
    -always returns same number of elemenets as original iterable. Filter() doesn't have this
    -map calls lambda function on all items, replacing a for loop:
                results = []
                x = ['Python', 'programming', 'is', 'awesome!']
                for item in x:
                    results.append(item.upper())

                print(results)
    """
    complaint_data = list(map(lambda arg: arg.upper(), df))
    return complaint_data


def filter_func(df):
    """
    -takes iterable, calls lambda function on each item and returns items where lambda returned true
    -replacing for loop function:
         def is_less_than_8_characters(item):
            return len(item) < 8
            x = ['Python', 'programming', 'is', 'awesome!']
            results = []

            for item in x:
                if is_less_than_8_characters(item):
                    results.append(item)

            print(results)
    -
    """
    return (list(filter(lambda arg : len(arg) < 8, df)))
     # return df.filter(lambda line : expression or function name(param))
    pass

def lower_case(df):
    return df.lower()

# def reduce_func(df):
#     """
#     -reduce applies to each element in your iterable
#     -reduce () doesn't return a new iterable, it uses the function called to reduce iterable into a signle value.
#     """
#     reduce_data = reduce(lambda val1, val2 : val1 + val2, df)
#     return reduce_data

def print_schema(df):
    return df.printSchema()

def describe_df(df):
    #gives dataframe description. column name and column type
    return df.describe()

def get_df_size(df):
    return df.count()

def df_size_report(df_list):
    row_dict = {}
    #prints total rows for each df
    for df in df_list:
        row_dict[df] = get_df_size(df)
    return row_dict

def get_df_log(df, num):
    #can select how many rows should be shown
    return df.show(n=num)

def get_df_rows(df, num):
    return df.take(num)

def get_column_info(df, col):
    #get count, mean, stddev, min, max for column
    return df.describe(col).show()

def drop_duplicate(df, col):
    #drop duplicates and sort in for column data
    return df.select(col).dropDuplicates().sort()