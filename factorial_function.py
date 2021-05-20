"""
Created on Tue Oct 31 10:31:45 2017

@author: cdib
"""

def factorial(n):
    """Calculate a factorial"""
    product = 1
    for i in range(1, n+1):
        product = product * i
    return product

def enter_positive():
    """Get the user to enter a positive integer"""
    n = - 1
    while n <= 0:
        n = int(input("Enter a positive integer: "))
    return n


number = enter_positive()
print(number, "! =", factorial(number))
