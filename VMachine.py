# -*- coding: utf-8 -*-
"""
Vending Machiiiiine!
"""
#//// Dictionaries/Variables ////
vm = {"C1":"Coke", "C2":"Sprite", "C3":"Fanta", "H1":"Coffee", "H2":"Tea", "H3":"Hot Chocolate", "S1":"Kitkat", "S2":"Cheetos", "S3":"Snickers"} #Dictionary for the vending machine stock with Code:Item Name
prices = {"Coke":0.5, "Sprite":0.5, "Fanta":0.5, "Coffee":2, "Tea":3, "Hot Chocolate":2, "Kitkat":1, "Cheetos":2.5, "Snickers":2} #Dictionary for prices with Item Name:Price
s = {"Coke":25, "Sprite":25, "Fanta":20, "Coffee":15, "Tea":20, "Hot Chocolate":10, "Kitkat":10, "Cheetos":2, "Snickers":8}#Dictionary for the vending machine's stock, with Item Name:Stock
combo = {"R1":"Coke and Cheetos", "R2":"Hot Chocolate and Kitkat", "R3":"Coffee and Snickers", "R4":"Coke, Sprite, and Fanta"}
money = 0
#//// Dictionaries/Variables ////

#/////Inventory Functions///
#This will show the current stock
def inventory():
    #Dictionary for the inventory, along with the info in string format
    inventory={ "C1":{"Price":"$0.5","Name":"Coke"},
                "C2":{"Price":"$0.5","Name":"Sprite"},
                "C3":{"Price":"$0.5","Name":"Fanta"},
                "H1":{"Price":"$2  ","Name":"Coffee"},
                "H2":{"Price":"$3  ","Name":"Tea"},
                "H3":{"Price":"$2  ","Name":"Hot Chocolate"},
                "S1":{"Price":"$1  ","Name":"KitKat"},
                "S2":{"Price":"$2.5","Name":"Cheetos"},
                "S3":{"Price":"$2  ","Name":"Snickers"}
                }
    print ("~~~~Here's what's available:~~~~")
    for code, info in inventory.items():
        print("\n", code, end=" ")
        
        for key in info:
            print(key + ':', info[key], end=" ")
    print ("\n")
    print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#This will show the current stock for the combo items
def comboinventory():
    #Dictionary for the inventory, along with the info in string format
    inventory={ "R1":{"Price":"$3  ","Name":"Coke and Cheetos"},
                "R2":{"Price":"$3  ","Name":"Hot Chocolate and Kitkat"},                
                "R3":{"Price":"$4  ","Name":"Coffee and Snickers"},
                "R4":{"Price":"$1.5","Name":"Coke, Sprite, and Fanta"}
                }
    print ("~~~~Here's what's available:~~~~")
    for code, info in inventory.items():
        print("\n", code, end=" ")
        
        for key in info:
            print(key + ':', info[key], end=" ")
    print ("\n")
    print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
#/////Inventory Function///

#/////Money Function/////
def creditsadd():
    #very important, this sets the variable to global so we can affect outside variables
    global money
    
#this is the function that adds money, the try statement will make sure that when the user types in non integers it won't error
    try:
        moneyadd = 0
        moneyadd += int(input("How much would you like to add?: "))
        if moneyadd > 0:
            money += moneyadd
        else:
            print("//// Please enter a valid amount. ////")
            creditsadd()
    except:
        print("//// Please enter a valid amount. ////")
        creditsadd()
    print ("$",moneyadd, " added, current credits: $",money, sep="")
#/////Money Function/////

#/////Buy Function/////
def buy():
    global money
    buyloop = True
    inventory() #calls the inventory function which shows the items available for purchase
    while buyloop == True: #buy function loop
        item = input("Please input the item code here:")  #lets you input the item code
        if item in vm: #input code is checked if it's in the vending machine's list of items
            itemname = vm[item]
            if s[itemname] > 0: #checks if the item has stock
                if money - prices[itemname] >= 0: #checks if you can afford the item
                    print ("~~~~~~~~~~Dispensing~~~~~~~~~~~~", "\n~~~~~ Enjoy your",vm[item],"~~~~~~") #dispenses the item after the above checks are true
                    money -= prices[itemname] #deducts money based on the item's price
                    print("Available funds: $", money) #shows the available remaining funds
                    s[itemname] += -1 #deducts stock
                    choice=input("Would you like to purchase something else? y/n: ") #lets the user input a choice to buy again
                    if choice == "y":
                        buyloop = True
                    else:
                        buyloop = False
                else:
                    print("//// Insufficient funds, please add more, and try again. ////")#error if there is less funds than the price
                    buyloop = False
            else:
                print("//// Out of stock, please try again. ////")#error if there is no remaining stock for the code given
                buyloop = False
        else:
                print("//// Invalid code, please try again. ////")#error if user inputs an invalid code
                buyloop = False
#/////Buy Function/////

#////Recommended Function////
def buyrec():
    global money
    recloop = True
    comboinventory() #calls the inventory function which shows the items available for purchase
    while recloop == True: #buy function loop
        item = input("Please input the item code here:")  #lets you input the item code
        if item in combo: #input code is checked if it's in the vending machine's list of items
            itemname = combo[item]
            if itemname == "Coke and Cheetos": #if checks for each combo
                comboprice = prices["Coke"] + prices["Cheetos"]
                if s["Coke"] and s["Cheetos"] >= 0: #checks for combo stock
                    comboprice = prices["Coke"] + prices["Cheetos"] #price of the combo
                    if money - comboprice >= 0:
                        print("~~~~~~~~~~Dispensing~~~~~~~~~~~~", "\n~ Enjoy your",combo[item],"~")
                        money -= comboprice
                        print("Available funds: $", money) #shows the available remaining funds
                        s["Coke"] += -1 #deducts stock
                        s["Snickers"] += -1 #deducts stock
                        choice=input("Would you like to purchase something else? y/n: ") #lets the user input a choice to buy again
                        if choice == "y":
                            recloop = True
                        else:
                            recloop = False
                    else:
                        print("//// Insufficient funds, please add more, and try again. ////")#error if there is less funds than the price
                        recloop = False
                else:
                    print("//// Sorry! One or more of the items in the combo is out of stock. ////")
                    recloop = False
            elif itemname == "Hot Chocolate and Kitkat": #if checks for each combo
                comboprice = prices["Hot Chocolate"] + prices["Kitkat"]
                if s["Hot Chocolate"] and s["Kitkat"] >= 0: #checks for combo stock
                    comboprice = prices["Hot Chocolate"] + prices["Kitkat"] #price of the combo
                    if money - comboprice >= 0:
                        print("~~~~~~~~~~Dispensing~~~~~~~~~~~~", "\n~ Enjoy your",combo[item],"~")
                        money -= comboprice
                        print("Available funds: $", money) #shows the available remaining funds
                        s["Hot Chocolate"] += -1 #deducts stock
                        s["Kitkat"] += -1 #deducts stock
                        choice=input("Would you like to purchase something else? y/n: ") #lets the user input a choice to buy again
                        if choice == "y":
                            recloop = True
                        else:
                            recloop = False
                    else:
                        print("//// Insufficient funds, please add more, and try again. ////")#error if there is less funds than the price
                        recloop = False
                else:
                    print("//// Sorry! One or more of the items in the combo is out of stock. ////")
                    recloop = False
            elif itemname == "Coffee and Snickers": #if checks for each combo
                comboprice = prices["Coffee"] + prices["Snickers"]
                if s["Coffee"] and s["Snickers"] >= 0: #checks for combo stock
                    comboprice = prices["Coffee"] + prices["Snickers"] #price of the combo
                    if money - comboprice >= 0:
                        print("~~~~~~~~~~Dispensing~~~~~~~~~~~~", "\n~ Enjoy your",combo[item],"~")
                        money -= comboprice
                        print("Available funds: $", money) #shows the available remaining funds
                        s["Coffee"] += -1 #deducts stock
                        s["Snickers"] += -1 #deducts stock
                        choice=input("Would you like to purchase something else? y/n: ") #lets the user input a choice to buy again
                        if choice == "y":
                            recloop = True
                        else:
                            recloop = False
                    else:
                        print("//// Insufficient funds, please add more, and try again. ////")#error if there is less funds than the price
                        recloop = False
                else:
                    print("//// Sorry! One or more of the items in the combo is out of stock. ////")
                    recloop = False   
            elif itemname == "Coke, Sprite, and Fanta": #if checks for each combo
                comboprice = prices["Coke"] + prices["Sprite"] + prices["Fanta"]
                if s["Coke"] and s["Sprite"] and s["Fanta"] >= 0: #checks for combo stock
                    comboprice = prices["Coffee"] + prices["Snickers"] #price of the combo
                    if money - comboprice >= 0:
                        print("~~~~~~~~~~Dispensing~~~~~~~~~~~~", "\n~ Enjoy your",combo[item],"~")
                        money -= comboprice
                        print("Available funds: $", money) #shows the available remaining funds
                        s["Coke"] += -1 #deducts stock
                        s["Sprite"] += -1 #deducts stock
                        s["Fanta"] += -1 #deducts stock
                        choice=input("Would you like to purchase something else? y/n: ") #lets the user input a choice to buy again
                        if choice == "y":
                            recloop = True
                        else:
                            recloop = False
                    else:
                        print("//// Insufficient funds, please add more, and try again. ////")#error if there is less funds than the price
                        recloop = False
                else:
                    print("//// Sorry! One or more of the items in the combo is out of stock. ////")
                    recloop = False
        else:
            print("//// Invalid code, please try again. ////")
            recloop = False
#////Recommended Function////

#/////Main Menu/////
def mainmenu():
    menuloop = True
    choice = 0
    global money
    while menuloop == True: #creates a loop for the main menu
        print ("~~~~~ Welcome to my Vending Machine! ~~~~~")
        print ("1 Insert Credits - Currently: $",money, sep="")
        print ("2 Purchase Items")
        print ("3 Purchase Combo Items")
        print ("4 Done")
        print("\n")
        try: #TRY here is important since the choice HAS to be an integer, if the the user uses a non integer, it will trigger an error, which we can bypass with the except statement
            choice = int(input("Please select an option: "))
            print ("\n")
            if choice == 4: #this gives the change if any, and exits the program
                if money > 0:
                    print ("Your change is $", money, " don't forget it!", sep="")
                    money == 0
                    print ("Thank you for your purchase! See you again!")
                    break
                else:
                    print ("See you again!")
                    break
            elif choice == 3: #calls the buyrec function for buying combos
                buyrec()
            elif choice == 2: #calls the buy function and shows the available items and lets the user input the code for what they want
                buy()
            elif choice == 1: #calls the function to add more money
                creditsadd()
            else:
                print("//// Invalid option, please try again. ////")
        except:#this will catch the error and print the below statement
            print("//// Invalid option, please try again. ////")
        print("\n")
#/////Main Menu/////

mainmenu()