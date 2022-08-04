import pandas as pd
from collections import Counter
import time
import operator
import random

consumer_complaints_data=pd.read_csv('/home/ra-terminal/datasets/complaints/complaints.csv')
subset_complaints=consumer_complaints_data.head(500000)
list_of_headers=subset_complaints.columns


def count_complaints_by_state1(df):
    state_comp_count={}                  
    for idx, row in df.iterrows():      
        state=row['State']               
        if state in state_comp_count:    
            state_comp_count[state] += 1 
        else:                            
            state_comp_count[state] = 1  
    return state_comp_count              

def count_complaints_by_state2(df):
    df['Point']=1                                                           
    state_comp_count_df = df.groupby('State')['Point'].sum().reset_index()  
    state_comp_count_df.set_index("State", drop=True, inplace=True)         
    state_comp_count_dict=state_comp_count_df.to_dict()['Point']            
    return state_comp_count_dict                                            

def count_complaints_by_state3(df):
    state_comp_count_dict=Counter(df['State'])
    return state_comp_count_dict              


def rank_times(runtime1, runtime2, runtime3):
    """
    Ranking the runtimes into a dictionary
    """
    runtimes={"runtime1":runtime1, "runtime2":runtime2, "runtime3":runtime3}
    sorted_runtimes = sorted(runtimes.items(), key=operator.itemgetter(1))
    return sorted_runtimes



def double_for_loop():
    total=0                     #1
    for i in range(0, 100):     #N
        for j in range(0, i):   #N *
            total=i+j           #N *
    return total                #1


if __name__=="__main__":
    print("-----------------------")
    start1=time.time()
    count_complaints1=count_complaints_by_state1(subset_complaints)
    end1=time.time()
    runtime1=end1-start1

    start2=time.time()
    count_complaints2=count_complaints_by_state2(subset_complaints)
    end2=time.time()
    runtime2=end2-start2

    start3=time.time()
    count_complaints3=count_complaints_by_state3(subset_complaints)
    end3=time.time()
    runtime3=end3-start3

    # print("count_complaints1: ",  runtime1, "count_complaints2: ",  runtime2, "count_complaints3: ",  runtime3)
    # print(rank_times(runtime1, runtime2, runtime3))
    print(double_for_loop())
    pass