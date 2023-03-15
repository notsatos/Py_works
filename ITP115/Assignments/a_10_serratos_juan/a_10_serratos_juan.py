# Juan Serratos, jserrato@usc.edu
# ITP 115, Fall 2022
# Section: 31865
# Assignment 10
# Description: We write a program that manages/creates a menu for the user to play with.

# We define a simple function to display the choices the user will have in main()
def displayChoices():
    print("Manage the menu\n  a) Add a menu item\n  b) Update the price\n  c) Show the price\n  d) Delete a menu item\n  e) Show the menu\n  x) Exit")
def isFloat(numStr):
    # We take out the deceimal in the float of numStr (if there is one)
    numStr = numStr.replace(".", "") 
    # Checking if we have a digit in the end to later use a quick checker that we have a digit.
    if numStr.isdigit():
        return True
    else:
        return False

def addItem(menuDict):
    input_0 = input("Enter a food item to add: ")
    input_0 = input_0.strip()
    # We get user input and take out the unnecessary spacing, and now we will inspect the first letter to
    # capitalize it as the instructions insist
    if input_0[0] == input_0[0].lower():
        input_0 = input_0.title()
    
    if input_0.lower() in menuDict:
        print(input_0,"is already on the menu")
    else:
        # We run through a dummy while loop to make sure we're getting valid input from 
        # the user, and then add the item to our dictionary menuDict
        dummy = 3
        while dummy == 3:
            priceInput = input("Enter the price: ")
            if isFloat(priceInput) == True:
                dummy +=1
        priceInput_2 = float(priceInput)
        menuDict[input_0.lower()] = priceInput_2
        print(input_0, "has been added to the menu.")
def updatePrice(menuDict):
    dummy = 1
    # Making another dummy while loop to get valid input from the user, 
    # and also inspecting capitalization as asserted in the instructions.
    while dummy == 1:
        input_0 = input("Enter a food item to update: ")
        input_0 = input_0.strip()
        if input_0[0] == input_0[0].lower():
            input_0 = input_0.title()
        # now we check our dictionary and start looking at values assigned
        # to things to display, and to change according to user input  
        if input_0.lower() in menuDict:
            print (input_0, "costs " + "$" + str (menuDict[input_0.lower()]))
            dummy2 = 2
            while dummy2 == 2:
                inputPrice = input("Enter the price: ")
                if isFloat(inputPrice) == True:
                    print(input_0, "now costs " + "$" +str(inputPrice))
                    menuDict[input_0.lower()] = inputPrice
                    dummy2+=2
                    dummy+=2
        else:
            print( input_0, "is not on the menu")
            dummy +=1

def showPrice(menuDict):
    dummy = 1 
    # A dummy while loop to find the values associated to
    # things in the dictionary.
    while dummy == 1:
        input_0 = input("Enter a food item to find: ")
        # if the item is in the dictionary then we print and show its associated value
        if input_0.lower() in menuDict:
            print(input_0.lower().strip().title(), "costs " + "$" + str(menuDict[input_0.lower()]))
            dummy +=2
        else:
            print(input_0.lower().strip().title(), "is not on the menu.")
            dummy +=2
def deleteItem(menuDict):
    dummy =1
    # Dummy while loop to delete items from our dictionary
    while dummy == 1:
        input_0 = input("Enter a food item to delete: ")
        # if the user gives us a food item that's in our dictionary then
        # we delete it
        if input_0.lower() in menuDict:
            del menuDict[input_0]
            print(input_0.lower().strip().title(), "was deleted from the menu.")
            dummy +=2
        else:
            print(input_0.lower().strip().title(), "is not on the menu")
            dummy +=2

def showMenu(menuDict):
    # Looking at the dictionary, we print eventhing inside of it
    # according to name and cost of the item
    for name, price in menuDict.items():
        print(name.title(), "costs $" +str(price))
def main():
    dict = {'pizza': 5.20, 'chicken': 12.00, 'coffee': 3.50}
    choice = "q"
    # The last dummy while loop to let the user use the displayed options/choices
    while choice == "q":
        displayChoices()
        inputChoice = input("Choice: ").lower().strip()
        if inputChoice == "a":
            addItem (dict)
        elif inputChoice == "b":
            updatePrice(dict)
        elif inputChoice == "c":
            showPrice(dict)
        elif inputChoice == "d":
            deleteItem(dict)
        elif inputChoice == "e":
            showMenu(dict)
        elif inputChoice == "x" or inputChoice == "X":
            choice = "x"
            print("Thank you")
        else:
            print("Invalid choice")
        
main()