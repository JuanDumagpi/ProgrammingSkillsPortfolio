# -*- coding: utf-8 -*-
"""
Exercise 5: USB Shopper
"""
#Variables for the USB Stick Price and the amount of money the girl has
USBPrice=6
GirlMoney=50

"""
Variable for the operation used to determine the amount of USB sticks.
Since the result is a decimal, used the round() function to convert it to a whole number
"""
USBs=round(GirlMoney/USBPrice)

#Prints variables as well as the answer
print("If the girl has £" ,GirlMoney ,"and each USB stick costs £" ,USBPrice 
      ,", then she can buy" ,USBs ,"USB sticks")
