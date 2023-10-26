# -*- coding: utf-8 -*-
"""
Chapter 7 - Functions
Ex 2 - Fave Book
"""
#In this function, there is an argument for (title), so when the function is called, it lets us set the argument
def Favorite_Book(title):
    print("My favorite book is ", title)

#Here we are calling the function with a specific argument, this will print out message in the function and use the argument to replace (title)
Favorite_Book("The Hobbit")
Favorite_Book("The Hitchhiker's Guide to the Galaxy")
Favorite_Book("House of Leaves")
