# -*- coding: utf-8 -*-
"""
Chapter 6 Loops
Exercise 2 - Movie Tickets
"""
#creates an infinite loop
while True:
    
    #input for age
    x = int(input("Please enter your age:"))

    #checks the input and prints the appropriate message
    if x<3:
        print ("Under 3, ticket's free!")
    elif x>=3 and x<=12:
        print ("Ticket is $10")
    else:
        print ("Ticket is $15")
    