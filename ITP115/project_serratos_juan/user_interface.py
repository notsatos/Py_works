# Juan Serratos, jserrato@usc.edu
# ITP 115, Fall 2022
# Section: 31865
# Final Project
# helper.py
# Description: We write a program that manages/creates function for the user to play with in the main file.
import helper

# This is how we will display the menu to the user as define in main()
def displayMenu(menuDict):
    # for the corresponding keys in menuDict, we get the 
    # value that it is and print it to the user
    for x in menuDict:
        print(str(x) + " -> " + menuDict[x])

def getUserChoice(menuDict):
    # We get user input so that it is stripped and whatnot and return it 
    input_0 = input("Choice: ").strip()
    x = input_0.strip().upper()
    return x 
def displayNumCoasters(coastersList):
    # We get the number of total coasters by counting how 'long' the coasterList is, and return it to the user
    lp = len(coastersList)
    return lp 
def displayNumOperatingCoasters(coasterDict):
    # we count how many dictionaries are operating
    count = 0
    # looking at the value of the key, "status", we're able to count
    # how many are operating and just keep ticking up our count
    for x in coasterDict:
        if x["status"] == "status.operating":
            count+=1 
    return count
def displayCoaster(coasterDict):
    # for a coaster in coasterDict,
    # we print the value of the keys with each key, that is,
    # we print the value of "name", "park", "speed", etc...
    for x in coasterDict:
        print(x["name"],"[" + x["park"] + "]")
        if x["speed"] !="":
            print("\tSpeed = " + x["speed"]+" mph")
        if  x["height"] !="":
            print("\tHeight = " + x["height"]+" ft")
        if  x["length"] !="":
            print("\tLength = " + x["length"]+" ft")
        if x["status"] == "status.operating":
            print("\tStatus is operating")
        elif x["status"] != "":
            print("\tStatus is", x["status"])
def displayFastestCoaster(coastersList):
    # we call our function getFastestCoaster to get it
    special = helper.getFastestCoaster(coastersList)
    # and then for the data, we begin to print information about it using dictionary
    # keys as we did in displayCoaster
    for x in coastersList:
        if x["name"]==special["name"]:
            print(x["name"],"[" + x["park"] + "]")
            if x["speed"] !="":
                print("\tSpeed = " + x["speed"]+" mph")
            if  x["height"] !="":
                print("\tHeight = " + x["height"]+" ft")
            if  x["length"] !="":
                print("\tLength = " + x["length"]+" ft")
            if x["status"] == "status.operating":
                print("\tStatus is operating")
            elif x["status"] != "":
                print("\tStatus is", x["status"])
def displayAllParks(coastersList):
    # we call the getParksList to get a list of all coasters so that we can sort them
    sorted = helper.getParksList(coastersList)
    print("Amusement parks in alphabetical order: ")
    for x in sorted:
        print(x)
    print("There are", len(sorted), "unique parks.")
def displayCoastersInPark(coastersList):
    # we get the user to give a name of a park and we strip it and make it 
    # lowercase.
    inp = input("Enter a park: ")
    x =inp.strip().lower()
    count = 0
    # we first fix a 'park' in the coasterList, then we 
    # check the userinput is apart of the value of the key for "park"
    for park in coastersList:
        if x in park["park"].lower():
            # if the user's input is in the value for the key for park, 
            # then we print the information of the coaster as done in displayCoasters
            print(park["name"], "[" + park["park"] + "]")
            if park["speed"] !="":
                print("\tSpeed = " + park["speed"]+" mph")
            if  park["height"] !="":
                print("\tHeight = " + park["height"]+" ft")
            if  park["length"] !="":
                print("\tLength = " + park["length"]+" ft")
            if park["status"] == "status.operating":
                print("\tStatus is operating")
            elif park["status"] != "":
                print("\tStatus is", park["status"])
            # we keep track of how many of user's input is the value for the key for park
            count+=1
    if count == 0:
        # if user's input is not in the value for any key for a park, then we return:
        print("No coasters in", inp.title())
    elif count > 0:
        # if there are user's input is in the value for the key for park then we print it
        print(inp.title(), "has", count, "coasters")
def findCoasters(coastersList):
    inp = input("Enter a search phrase: ")
    x =inp.strip().lower()
    count = 0
    # This is almost exactly the same as  displayCoastersInPark 
    # except we search if the user's input is park["name"]
    # rather than  park["park"] in displayCoastersInPark.
    for park in coastersList:
        if x in park["name"].lower():
            print(park["name"], "[" + park["park"] + "]")
            if park["speed"] !="":
                print("\tSpeed = " + park["speed"]+" mph")
            if  park["height"] !="":
                print("\tHeight = " + park["height"]+" ft")
            if  park["length"] !="":
                print("\tLength = " + park["length"]+" ft")
            if park["status"] == "status.operating":
                print("\tStatus is operating")
            elif park["status"] != "":
                print("\tStatus is", park["status"])
            count+=1
    if count == 0:
        print("No coasters contain " +"'"+inp.title()+"'")
    elif count > 0:
        print("Found", count, "coasters that contain " +"'"+inp.title()+"'")


    