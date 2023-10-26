# -*- coding: utf-8 -*-
"""
Chapter 7 - Functions
Ex 5 - Cities
"""
#this defines a function to print a statement with default arguments
def describe_city(name="New York", country="USA"):
    print (name, "is in", country)

#calls the describe_city function which will print the message above, since there are no values for arguments, it will default
describe_city()

#these will will call the describe_city function but changes the arguments, so it will not default
describe_city("Manila", "Philippines")
describe_city("Paris", "France")
