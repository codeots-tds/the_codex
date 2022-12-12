def generate_lists_of_lists(n):
    table_list = []
    for num in range(n):
        row = []
        for i in range(n):
            row.append(i)
        table_list.append(row)
    return table_list


def sum_nums1(num_list):
    total = 0               #1
    for lst in num_list:    #T
        for num in lst:     #T * V
            total += num    #T
    return total            #1
                            #Space Complexity: O(T*V)

def sum_nums2(num_list):    
    total = 0               #1
    for nums in num_list:   #T
        total += sum(nums)  #T
    return total            #1
                            #Space Complexity: O(T)


if __name__ == "__main__":
    lists_of_nums_list = generate_lists_of_lists(10)
    total_sum1 = sum_nums1(num_list = lists_of_nums_list)
    print(total_sum1)
    total_sum2 = sum_nums2(num_list = lists_of_nums_list)
    print(total_sum2)