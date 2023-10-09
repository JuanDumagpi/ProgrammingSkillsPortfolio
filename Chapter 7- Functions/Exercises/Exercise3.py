# -*- coding: utf-8 -*-
"""
Chapter 7 - Functions
Ex 3 - TShirt
"""

def make_shirt(size, message):
    print ("Size:", size, "\n", "Message:", message)

#positional arguments
make_shirt("Medium", "It's Premium!")

print("\n")

#keyword arguments don't care about position
make_shirt(message="It's in charge.", size="Large")