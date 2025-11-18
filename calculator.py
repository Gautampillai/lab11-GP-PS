# https://github.com/Gautampillai/lab11-GP-PS
# Partner 1: Gautam Pillai
# Partner 2: Priya Schramm

import math

def square_root(a):
    if a < 0:
        raise ValueError("Value has to be greater or equal to 0")
    return math.sqrt(a)  # raise ValueError if a < 0

def hypotenuse(a, b):
    return math.hypot(a, b) # can have negative nums

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return b / a # raise ZeroDivisionError if a == 0

def logarithm(a, b):
    if a <= 0 or b <= 0:
        raise ValueError("Log undefined for negative values")
    return math.log(b, a)# use math library + raise ValueError

def exp(a, b):
    return a**b