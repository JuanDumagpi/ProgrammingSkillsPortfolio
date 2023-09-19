# -*- coding: utf-8 -*-
"""
Exercise 5: Compute area of Circle 
"""

#imports the value of pi
from math import pi

#float variable, so the number can be a decimal, int if we want to restrict it to whole numbers
#input let's the user type in their choice of number
r = float(input ("Please input the radius:"))

#Shows the chosen radius, as well as the answer. * is used for multiplication, ** is used for exponents.
print ("The area of a circle with a radius of" ,r ,"is" ,(pi * r**2))

