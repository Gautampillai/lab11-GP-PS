import math

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError("denominator can't be 0")
    return b / a # raise ZeroDivisionError if a == 0

def log(a, b):
    if a <= 1:
        raise ValueError("Base has to be greater than 1")
    return math.log(b, a)# use math library + raise ValueError

def exp(a, b):
    return a**b