# -*- coding: utf-8 -*-
"""
Stages of Life
"""

age = int(input("Please enter your age: "))

if age<2: #if the age is less than 2, print below message
    print("You're a baby.")

elif age>2 and age<4: #if the age is greater than 2 but less than 4, print below message
    print ("You're a toddler.")

elif age>=4 and age<13: #if the age is greater than or equal to 4 but less than 13, print below message
    print ("You're a kid.")

elif age>=13 and age<20: #if the age is greater than or equal to 13 but less than 20, print below message
    print ("You're a teenager.")

elif age>=20 and age<65: #if the age is greater than or equal to 20 but less than 65, print below message
    print ("You're an adult.")

else: #if the age is greater than 65, print below message
    print("You are old.")