#importing from same level directory
from .basic_calculator import add

#importing from nested sub-directory to a script in a grandparent directory
from .special_funcs.more_special_funcs.even_more_funcs.special_calc_3 import circum_circle
#this works when you're in your root project directory
#Must run 'python -m calc.basic_calculator2'


def mult(x1, x2):
    return x1 * x2

def divide(m1, m2):
    return m1 / m2

if __name__ == "__main__":
    print(add(5,7))
    print(add(9,12))
    pass