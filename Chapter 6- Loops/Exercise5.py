# -*- coding: utf-8 -*-
"""
Chapter 6
Exercise4 - Deli
"""
#list of orders
sandwhich_orders=["PB&J", "Grilled Cheese", "Tuna","Pastrami","Pastrami", "Pastrami"]

#a message that says Pastrami is sold out
print("ATTENTION: Pastrami is 86")

#This makes a loop that looks for all Pastrami in the sandwhich_orders list then removes all the Pastrami
while "Pastrami" in sandwhich_orders:
    sandwhich_orders.remove("Pastrami")

#prints a message that shows the updated list
print (sandwhich_orders)
