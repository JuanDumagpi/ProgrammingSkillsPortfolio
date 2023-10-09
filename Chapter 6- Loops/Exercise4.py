# -*- coding: utf-8 -*-
"""
Chapter 6
Exercise4 - Deli
"""
#list of orders and finished orders
sandwhich_orders=["PB&J", "Grilled Cheese", "Tuna",]
finished_sandwhiches=[]

#this prints the current list
print("Current orders: ", sandwhich_orders)
print("Finished orders: ", finished_sandwhiches)
print("\n")

#loop that checks the amount of items in the sandwhich_orders list
for x in range(len(sandwhich_orders)):
    
    #variable that pops an item in sandwhich_orders, and prints a message to identify it
    queue = sandwhich_orders.pop()
    print(queue, "is being made.")
    
    #this adds the specific item from queue to finished_sandwhiches
    finished_sandwhiches.append(queue)
    
    #this prints the lists everytime an item is moved.
    print("Current orders: ", sandwhich_orders)
    print("Finished orders: ", finished_sandwhiches)
    print("\n")