# https://github.com/calumgreaser-gif/lab11--CG-
# Calum Greaser
# My partner left to join another group without informing me first, so when I reached out to a TA, they said it would be alright if I did this project on my own.

"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""

import math

# First example
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if a == 0:
        raise ZeroDivisionError("a cannot be zero")
    return b / a

def logarithm(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError("Invalid argument for logarithm")
    return math.log(b, a)

def exponent(a, b):
    return a ** b