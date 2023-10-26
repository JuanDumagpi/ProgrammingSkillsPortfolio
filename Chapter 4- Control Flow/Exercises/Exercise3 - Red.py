# -*- coding: utf-8 -*-
"""
Alien Colors #3
red
"""

#sets alien color
alien_color = "red"

#this tests if the alien color is green and if true, displays a message
if alien_color == "green": #checks if the color is green and if true, prints the below message
    print ("You obtain 5 points")
#elif tests a different condition of the if-statement
elif alien_color == "yellow": #checks if the color is yellow and if true, prints the below message
        print ("You obtain 10 points")
        
elif alien_color == "red": #checks if the color is red and if true, prints the below message
        print ("You obtain 15 points")
        
else: #if any of the above statements are not met, prints the below message
    print ("You obtain 0 points")
