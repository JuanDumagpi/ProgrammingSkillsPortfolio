# -*- coding: utf-8 -*-
"""
Chapter 6 Loops
Exercise 2 - Movie Tickets
"""
#creates an infinite loop
while True:
    
    #lets the user type in their age
    x = int(input("Please enter your age:"))

    #checks the age input and prints the appropriate message
    if x<3: #if the age is less than 3, prints the message below
        print ("Under 3, ticket's free!")
    elif x>=3 and x<=12: #if the age is equal to three but less than or equal to 12, prints the message below
        print ("Ticket is $10")
    else: #if it's not any of the above, prints the message below
        print ("Ticket is $15")
    
