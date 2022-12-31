import pandas as pd
#Absolute Imports
from module2 import pi #module I created
from math import sqrt #python in-built module
from calc.basic_calculator import add #module I created

from calc.special_funcs.special_calc import abs_value
from calc.special_funcs.more_special_funcs.even_more_funcs.special_calc_3 import circum_circle 

#Relative Imports
import sys
print(sys.path)

sys.path.append('/home/ra-terminal/Desktop/projects/medium_projects/imports_in_python\
/calc/special_funcs/more_special_funcs')


if __name__ == "__main__":
    print(pi)
    print(add(pi, 4))
    print(sqrt(25))
    print(abs_value(-4))
    print(circum_circle(4, 3))