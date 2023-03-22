import pandas as pd


""".apply()"""
test_grades = [60, 80, 85, 80, 90, 100, 105, 95, 90]
hw_grades = [50, 60, 85, 90, 100, 80, 90, 70, 90]
students = ['Suzy', 'Rob', 'John', 'Salim', 'Holland', 'Howard', 'Carl', 'Serena', 'Megan']
col_names = ['Students', 'Hw_Grades', 'Test_Grades']

student_perf_df = pd.DataFrame(list(zip(students, hw_grades, test_grades)),
                               columns = col_names)

def calc_avg(num1, num2):
    return num1+num2/2

avg_scores = []
for idx, row in student_perf_df.iterrows():
   student_perf_df.loc[idx, 'Avg'] = calc_avg(row['Hw_Grades'], row['Test_Grades'])

# avg_scores =  student_perf_df.apply(
#        lambda row: calc_avg(row['Hw_Grades'], 
#         row['Test_Grades']), axis=1)
# student_perf_df['Avg'] = avg_scores

print(student_perf_df)


"""------------------------------------------------------"""
"""Zip"""

"""Zip Two lists"""
names = ['Cloud', 'Bruce', 'Clark', 'Grant', "Lana", "Sora", 'Thanos', 'Tony']
age = [25, 30, 32, 15, 76, 26, 28, 42]

mapped_2_lists = list(zip(names, age))
# print("Zip mapping names and age", mapped_2_lists)

"""Zip Iterator Tuple Values"""
print("""Zip Iterator Tuple Values""")
# for idx, (name, age) in enumerate(zip(names, age)):
#     print(idx, name, age)

"""Zip Dictionary"""
video_games = ['God of War 4', 'Rainbow 6 Siege', 'Assassins Creed: Vikings']
game_prices = [60.00, 20.00, 40.00]

game_price_dict = {video_games: game_prices for video_games, game_prices 
                   in zip(video_games, game_prices)}
# print("Zipped Game Dict", game_price_dict)


"""------------------------------------------------------"""
"""Lambda"""

"""Lambda Average"""
num_list = [87, 34, 1, 55, 23, 34, 22, 67, 48, 29, 10, 26]
def calc_avg(num_list):
    return int(sum(num_list)/len(num_list))

lambda_avg = lambda number_list: int(sum(number_list)/len(number_list))

# print('Standard Avg Function:', calc_avg(num_list), 
#       'Lambda Avg Function:', lambda_avg(num_list))


"""Lambda Square"""
def square_num(num1):
    return num1 ** 2

lambda_square = lambda num1: num1 ** 2
# print('Standard Square Num:', square_num(5), 
#       'Lambda Square Num:', square_num(5))

"""Lambda Odd Number"""
odd_num = lambda num: "even num" if num % 2 == 0 else "odd num"
# print('Lambda Odd Number', odd_num(5))

"""Lambda Sorting"""
num_list2 = [43,12,67,89,11,44,0, 98,86,53,67]
lambda_sorting_list = sorted(num_list2, key=lambda x: int(x))
# print("Lambda Sorting", lambda_sorting_list)

"""------------------------------------------------------"""
"""Filter"""
num_list3 = [22, 34, 68, 29, 19, 20, 50, 57, 97, 98, 25, 31, 33, 84]
def is_even(num_int):
    if num_int % 2 == 0:
        return True
    else:
        return False

filtered_even_list = filter(is_even, num_list3)
# print("Filtered List", list(filtered_even_list))

"""Filter + Lambda"""
def is_odd(num_int):
    if num_int % 2 == 0:
        return False
    else:
        return True

odd_list = list(filter(lambda x: is_odd(x), num_list3))
# print("Filter + Lambda Odd Numbers", odd_list)

"""------------------------------------------------------"""
"""Map"""
num_list4 = [1, -1, 5, -10, 20, -60, -80, 30, 23, 56, 91, -99]
def multiply_4(n):
    return n * 4

#need to wrap in list function to avoid returning memory location
muliplied_by_4_list = list(map(multiply_4, num_list4))
# print("Lambda", muliplied_by_4_list)

"""Map + Lambda"""
multiplied_by_4_list_lambda = list(map(lambda x: x * 4, num_list4))
# print("Map + Lambda", multiplied_by_4_list_lambda)

"""Map + Lambda"""
price = [981.00, 876.75, 573.25, 142.50]
discounts = [.15, .25, .30, .50]
coupons = [5.00, 20.00, 30.00, 15.00]

total_prices = list(map(lambda x, y, z : x*y-z, price, discounts, coupons))
# print("Lambda Calculating Total Prices", total_prices)

"""Map List Elements in a List"""
cereal = ['Coco Puffs', 'Cinnamon Toast Crunch', 'Fruity Pebbles', 
          'Cookie Crisp', 'Chex', 'Kix']

listified_cereal = list(map(list, cereal))
# print('Listified Cereal', listified_cereal)



"""--------------------------------------------------"""
"""Reduce"""
from functools import reduce

home_prices = [450000.00, 800000.00, 1200000.00, 540500.00, 10400500.00, 2030000.00]
down_payment = [.10, .15, .20, .30, .10, .035]
monthly_payment_30 = 360

downpayment_for_homes = list(map(lambda x, y: x * y, home_prices, down_payment))
monthly_payments_30y = list(map(lambda x : int(x/monthly_payment_30), home_prices))

total_value_of_owned_homes = reduce(lambda x, y : x + y, home_prices)


# print("House Downpayments: ", downpayment_for_homes)
# print('Monthly Payments Over 30 Years: ', monthly_payments_30y)
# print('Total Inventory Value: ', total_value_of_owned_homes)


if __name__== "__main__":
    pass