# -*- coding: utf-8 -*-
"""
Vending Machiiiiine!
"""

C1 ={
     "Code" : "C1",
     "Item" : "Coke",
     "Price" : 1,
     "Stock" : 1,
     }
C2 ={
     "Code" : "C2",
     "Item" : "Sprite",
     "Price" : 1,
     "Stock" : 15,
     }
C3 ={
     "Code" : "C3",
     "Item" : "Fanta",
     "Price" : 1,
     "Stock" : 10,
     }
H1 ={
     "Code" : "H1",
     "Item" : "Coffee",
     "Price" : 2,
     "Stock" : 20,
     }
H2 ={
     "Code" : "H2",
     "Item" : "Tea",
     "Price" : 3,
     "Stock" : 5,
     }
H3 ={
     "Code" : "H3",
     "Item" : "Hot Chocolate",
     "Price" : 2,
     "Stock" : 5,
     }

itemlist = [C1, C2, C3, H1, H2, H3]
money = 0

#/////Inventory Function///
#This will show the current stock
def inventory():
    for item in itemlist:
        if item.get("Stock") == 0:
            itemlist.remove(item)
    for item in itemlist:
        print ("Code: ", item.get("Code"), " - ", "$",item.get("Price"), " ", item.get("Item"), " -", " Stock: ", item.get("Stock"), sep='')
    print("\n")
#/////Inventory Function///



#/////Money Function///
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
    print ("$",moneyadd, "added, current credits: $",money, sep="")
#/////Money Function///


#/////Main Menu/////
def mainmenu():
    menuloop = True
    choice = 0
    global money
    while menuloop == True:
        print ("1 Insert Credits - Currently: $",money, sep="")
        print ("2 Purchase Items")
        print ("3 Done")
        print("\n")
        try:
            choice = int(input("Please select an option: "))
            print ("\n")
            if choice == 3: #this gives the change if any, and exits the program
                if money > 0:
                    print ("Your change is $", money, " don't forget it!", sep="")
                    money == 0
                    print ("Thank you for your purchase! See you again!")
                    break
                else:
                    print ("See you again!")
                    break
            elif choice == 2: #shows the available items and lets the user input the code for what they want
                print ("~~~~Here's what's available:~~~~ \n")
                inventory()
                buy=input("Select item: ")
                print("\n")
                for item in itemlist: #goes through each dictionary looking for the code
                    if buy == item.get("Code"):
                        buy = item
                        price = buy.get("Price") #gets the price value from its key
                        if money < price: #checks if you have enough money
                            print ("//// Insufficient funds ////")
                            break
                        else:
                            print ("~~~~~~~~~~Dispensing~~~~~~~~~~")
                            print ("~~Enjoy your ", buy.get("Item"),"!~~", sep="")
                            buy["Stock"] -= 1
                            money -= price
                            print ("Remaining credits: ", "$", money, sep="")
                            print ("\n")
                            print ("Thank you for your purchase!")
            elif choice == 1: #calls the function to add more money
                creditsadd()
            else:
                print("//// Invalid option, please try again. ////")
        except:
            print("//// Invalid option, please try again. ////")
        print("\n")
#/////Main Menu/////
print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print ("|            Welcome to my           |")
print ("|           Vending Machine          |")
print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
inventory()
mainmenu()