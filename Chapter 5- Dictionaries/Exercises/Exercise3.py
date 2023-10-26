# -*- coding: utf-8 -*-
"""
Dictionaries
Exercise 3: Glossary2
"""

#this is the dictionary and keys
glossary = {
    "Print": "This displays a message!",
        
    "Variable": "Stores data values such as strings, integers, etc.",
    
    "Conditions": "Uses true or false logic to to evaluate a certain statement",
            
    "Dictionary": "Stores data values in Key:Value pairs",
    
    "Operators": "Performs operations on values and variables for logical and arithmetic operations",
    
    "Loop": "Repeats a block of code",
    
    "For": "A type of loop that is used to iterate sequences such as lists, tuples, string, etc",
    
    "While": "Repeats code until the condition is satisfied",
    
    "String": "Data that represents a sequence of characters.",
    
    "Float": "Data number that can be a decimal",
    }

#loop that checks the 'glossary' dictionary and prints each key and value formatted in a certain way
#x being the key variable and y being the value variable
for x,y in glossary.items():
    print(x, "\n \t", y, "\n")
