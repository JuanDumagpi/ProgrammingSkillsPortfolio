# -*- coding: utf-8 -*-
"""
Chapter 6
Exercise4 - Deli
"""
#list of orders
sandwhich_orders=["PB&J", "Grilled Cheese", "Tuna","Pastrami","Pastrami", "Pastrami"]

print("ATTENTION: Pastrami is 86")

#This makes a loop that looks for all Pastrami  then removes Pastrami
while "Pastrami" in sandwhich_orders:
    sandwhich_orders.remove("Pastrami")
    
print (sandwhich_orders)