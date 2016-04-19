import math
from random import randint, choice
import numbers
from fractions import Fraction

asdf = True

options = {'+': Fraction.__add__,
           '-': Fraction.__sub__,
           '*': Fraction.__mul__,
           '/': Fraction.__truediv__}
option_list = list(options.keys())

while True:
    a = Fraction(randint(0,12))
    b = Fraction(randint(1,12))
    op = option_list[randint(0,3)]
    print("{}{}{} = ".format(a,op,b), end="")
    solution = input()
    answer = options[op](a,b)
    try:
        if answer == Fraction(solution):
            print("Correct!")
        else:
            print("Nope!")
            continue
    except Exception as e:
        print("Give valid input next time!")
        break
