"""
Created on Tue Oct 10 16:12:55 2017

@author: cdib
"""

# A program to calculate the GCD of two non-negative integers

number_a = int(input("Enter a number: "))
number_b = int(input("Enter a second number: "))


if number_a == 0:
    GCD = number_b
    
if number_b == 0:
    GCD = number_a

if number_a == number_b:
    GCD = number_a

if number_b > number_a:
    c = number_a
    number_a = number_b
    number_b = c

if number_a >= number_b and number_b > 0: 
    remainder = (number_a % number_b)
    remainder_2 = (number_b % remainder)
    while remainder_2 >= 1:
        remainder_2 = (remainder % remainder_2)
        
    GCD = remainder_2

print("The greatest common divisor of", number_a, "and", number_b, "is", GCD)
    
