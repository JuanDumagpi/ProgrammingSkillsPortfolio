# -*- coding: utf-8 -*-
"""
Dictionaries
Exercise 5: pets
"""
#pet dictionaries
pet1 = {
    "Species": "Dog",
        
    "Owner": "Fuwawa",
    
    "Name": "Mococo",
    
    }

pet2 = {
    "Species": "Chinchilla",
        
    "Owner": "Mike",
    
    "Name": "Chami",
    
    }

pet3 = {
    "Species": "Cat",
        
    "Owner": "Korone",
    
    "Name": "Okayu",
    
    }

#list of dictionaries
petlist = [pet1, pet2, pet3]


#this loops a message for each dictionary in the list
for x in petlist:
    print(x)