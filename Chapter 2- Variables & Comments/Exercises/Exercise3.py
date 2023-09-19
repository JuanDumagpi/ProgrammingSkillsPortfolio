# -*- coding: utf-8 -*-
"""
Exercise 3: Stripping Names
"""
#Variable with extra whitespace on both sides and a line break in the middle
a="\t\t Peter \n Parker \t\t"
#Printed statement that shows the extra white space
print(a, "is spiderman.")

#extra space for visibility
print("\n")

#New variables that use the strip function to remove the extra spacing
strip1=a.strip() #strips both sides of the string
strip2=a.lstrip() #strips only the left side
strip3=a.rstrip() #strips only the right side

#printed messages that shows the stripped name
print(strip1, "is spiderman.")

#extra space for visibility
print("\n")

print(strip2, "is spiderman.")

#extra space for visibility
print("\n")

print(strip3, "is spiderman.")