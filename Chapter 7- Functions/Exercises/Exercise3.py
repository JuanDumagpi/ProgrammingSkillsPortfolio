# -*- coding: utf-8 -*-
"""
Chapter 7 - Functions
Ex 3 - TShirt
"""
#This defines the function to print a message with the arguments for (size), and (message)
def make_shirt(size, message):
    print ("Size:", size, "\n", "Message:", message)

#positional arguments let you change the arguments based on order, in this case (size) first before (message)
make_shirt("Medium", "It's Premium!")

print("\n")

#keyword arguments don't care about position, so you can choose too swap their orders as long as you add the argument you are calling to
make_shirt(message="It's in charge.", size="Large")
