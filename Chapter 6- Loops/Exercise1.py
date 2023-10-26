# -*- coding: utf-8 -*-
"""
Chapter 6 Loops
Exercise 1 - Pizza Toppings
"""
#empty list of toppings
ptop = []

#creates an infinite loop until broken
while True:
    
    #lets the user add toppings by typing down what they want
    x = input("Enter what you want to put on your pizza or type 'Done' to finish:")
    #this checks if they user has typed "Done", if true, then breaks the loop
    if x == "Done":
        break
    #adds the user's input to the topping list and displays a message, [-1] being the most recent item in the list 
    else:
        ptop.append(x)
        print(ptop[-1], "has been added to your pizza.")
        
#prints the pizza toppings list
print ("Your pizza toppings are: ", ptop)
