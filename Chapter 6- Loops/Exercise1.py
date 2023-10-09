# -*- coding: utf-8 -*-
"""
Chapter 6 Loops
Exercise 1 - Pizza Toppings
"""
#empty list of toppings
ptop = []

#creates an infinite loop until broken
while True:
    
    #input for pizza toppings
    x = input("Enter what you want to put on your pizza or type 'Done' to finish:")
    #checks if the input is done and breaks the loop
    if x == "Done":
        break
    #adds the input to the list if not done
    else:
        ptop.append(x)
        print(ptop[-1], "has been added to your pizza.")
        
#prints the pizza toppings list
print ("Your pizza toppings are: ", ptop)