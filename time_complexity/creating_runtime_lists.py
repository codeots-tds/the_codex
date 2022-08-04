from time_complex import consumer_complaints_data, count_complaints_by_state1, count_complaints_by_state2, count_complaints_by_state3
import random
import time
from charts import plot_line_chart, plot_line_chart2
import matplotlib.pyplot as plt


def get_random_num_list(num, start = 1000, end = 950000):
    """
    Getting random data size inputs to filter dataframe
    """
    arr = []
    tmp = random.randint(start, end)
    for x in range(num):
        while tmp in arr:
            tmp = random.randint(start, end)
        arr.append(tmp)
    arr.sort()
    return arr


def get_runtimes_list(df):
    """
    measuring runtimes
    """
    random_num_rows_list=get_random_num_list(10)

    num_rows1=[]
    runtime_list1=[]

    num_rows2=[]
    runtime_list2=[]

    num_rows3=[]
    runtime_list3=[]

    for random_num in random_num_rows_list:
        filtered_row_df = df.head(random_num)
        num_rows1.append(filtered_row_df.shape[0])
        start1=time.time()
        count_complaints1=count_complaints_by_state1(filtered_row_df)
        end1=time.time()
        runtime1=end1-start1
        runtime_list1.append(runtime1)

        num_rows2.append(filtered_row_df.shape[0])
        start2=time.time()
        count_complaints2=count_complaints_by_state2(filtered_row_df)
        end2=time.time()
        runtime2=end2-start2
        runtime_list2.append(runtime2)
        
        num_rows3.append(filtered_row_df.shape[0])
        start3=time.time()
        count_complaints3=count_complaints_by_state3(filtered_row_df)
        end3=time.time()
        runtime3=end3-start3
        runtime_list3.append(runtime3)
        

    count_complaints1_dict=dict(zip(num_rows1, runtime_list1))
    count_complaints2_dict=dict(zip(num_rows2, runtime_list2))
    count_complaints3_dict=dict(zip(num_rows3, runtime_list3))
    return count_complaints1_dict, count_complaints2_dict, count_complaints3_dict

if __name__=="__main__":
    count1_dict, count2_dict, count3_dict = get_runtimes_list(consumer_complaints_data)
    print("Counting Complaints by State Using For Loop:", count1_dict)
    print("--------------------------")
    print("--------------------------")
    print("Counting Complaints by State Using Pandas", count2_dict)
    print("--------------------------")
    print("--------------------------")
    print("Counting Complaints by State Using Counter Library", count3_dict)

    # plot_line_chart(algo_type="For Loop", num_rows=list(count1_dict.keys()), times=list(count1_dict.values()))
    # plot_line_chart(algo_type="Pandas", num_rows=list(count2_dict.keys()), times=list(count2_dict.values()))
    # plot_line_chart(algo_type="Counter", num_rows=list(count3_dict.keys()), times=list(count3_dict.values()))
    plot_line_chart2(dict1=count1_dict, dict2=count2_dict, dict3=count3_dict)
    # pass