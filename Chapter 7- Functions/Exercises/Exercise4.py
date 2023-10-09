# -*- coding: utf-8 -*-
"""
Chapter 7 - Functions
Ex 5 - TShirt
"""
#Defualt arguments added
def make_shirt(size = "Large", message="I love Python"):
    print ("Size:", size, "\n", "Message:", message)

make_shirt(size = "Medium")
print("\n")
make_shirt()
print("\n")
make_shirt(message="Is Justice.", size="Small")