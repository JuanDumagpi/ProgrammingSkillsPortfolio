# -*- coding: utf-8 -*-
"""
Chapter 7 - Functions
Ex 5 - TShirt
"""
#Default arguments added, which means, there is going to be a set value for the argument if no new ones are specified
def make_shirt(size = "Large", message="I love Python"):
    print ("Size:", size, "\n", "Message:", message)

#Here, it prints a message that changes the (size), but not the message which will then use the default 
make_shirt(size = "Medium")
print("\n")
#Here, it prints a message. Since there are no changes to the argument, will use the default
make_shirt()
print("\n")
#this changes both size and message, so it will not use the default
make_shirt(message="Is Justice.", size="Small")
