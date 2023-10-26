# -*- coding: utf-8 -*-
"""
Dictionaries
Exercise 4: Rivers
"""
#variable for the dictionary of rivers, with the key being the river's name and the value being where their location is
rivers = {
    "Amazon": "Brazil",
        
    "Mekong": "Thailand",
    
    "Congo": "Republic of Congo",
    
    }

#prints the statement "(key) flows through the country of (value)"
for x,y in rivers.items():
    print(x, "flows through the country of", y, "\n")

#prints the keys in the rivers dictionary    
for x in rivers:
    print(x)
    
print("\n")   
    
#prints the values in the rivers dictionary
for y in rivers.values():
    print(y)
