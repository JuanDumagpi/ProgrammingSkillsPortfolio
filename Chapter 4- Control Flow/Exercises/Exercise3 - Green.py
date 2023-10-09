# -*- coding: utf-8 -*-
"""
Alien Colors #3
green
"""

#sets alien color
alien_color = "yellow"

#this tests if the alien color is green and if true, displays a message
if alien_color == "green":
    print ("You obtain 5 points")
#elif tests a different condition of the if-statement
elif alien_color == "yellow":
        print ("You obtain 10 points")
        
elif alien_color == "red":
        print ("You obtain 15 points")
        
else:
    print ("You obtain 0 points") #this shows a message if the if statement is false
