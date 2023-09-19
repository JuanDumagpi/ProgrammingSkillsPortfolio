# -*- coding: utf-8 -*-
"""
IF CONDITION
"""

#AGE INPUT
age=int(input("Please enter your age "))
if age<=4:
    print("You're too young mate, get your parents.")
else:
    print("Welcome, kid.")
    
print("\n")
a=int(input("Enter a number to check for even or odd "))
if (a%2==0):
    print(a, "is an even number")
else:
    print(a, "is an odd number")