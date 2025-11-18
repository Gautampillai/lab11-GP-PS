import math

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return b / a # raise ZeroDivisionError if a == 0

def log(a, b):
    if a <= 0 or b <= 0:
        raise ValueError("Log undefined for negative values")
    return math.log(b, a)# use math library + raise ValueError

def exp(a, b):
    return a**b