# Juan Serratos, jserrato@usc.edu
# ITP 115, Fall 2022
# Section: 31865
# Final Project
# final_project.py
# Description: We make a roller coaster menu that the user can use to find and display 
# certain facts inside the roller_coaster.csv
# # THERE IS AN ERROR WITH MY COMPUTER/PYTHON THAT DOESN'T SEEM TO SEE THE COASTER.CSV IN THE SAME FOLDER SO 
# IT NEEDS A MORE DESCRIPTIVE PATH. PLEASE CHANGE TO NORMAL "roller_coasters.csv"  WHEN GRADING.
import user_interface
import helper

# We make a short dictionary, as the instructions describe to do, to later display the dictionary
# using functions we've defined in our other files.
def getMenuDict():
    dictio = { 
        'A' : 'Number of coasters',
        'B' : 'Number of operating coasters',
        'C' : 'Fastest coaster',
        'D' : 'Amusement parks',
        'E' : 'Coasters in a park',
        'F' : 'Find coasters',
        'Q' : 'Quit'
    }
    return dictio 

# We define our main function as described in the instruction, where we create a loop until the user decides to 
# quit the roller coaster menu
def main():
    print("Roller Coasters")
    coasters = helper.createCoastersFromFile()
    # This is a dummy number to change once we get an input of 'q'
    dummy = 0
    while dummy == 0:
        # getting our menu 
        menu = getMenuDict()
        # displaying our menu from the user_interface.py file
        user_interface.displayMenu(menu)
        # we get user input in a nice way by making it all lower case and stripping, 
        user_choice = user_interface.getUserChoice(menu).lower().strip()
        # we make sure the input is valid by going through the labels of our dictionary
        while user_choice.lower().strip() not in ['a', 'b', 'c', 'd', 'e', 'f', 'q']:
            user_choice = user_interface.getUserChoice(menu).lower().strip()
        # now we just align the input with functions that we have already made in user_interface.py
        if user_choice.lower().strip() == "a":
            print("The total number of coasters is", user_interface.displayNumCoasters(coasters))
        elif user_choice.lower().strip() == "b":
            print("The total number of operating coasters is", user_interface.displayNumOperatingCoasters(coasters))
        elif user_choice.lower().strip() == "c":
            user_interface.displayFastestCoaster(coasters)
        elif user_choice.lower().strip() == "d":
            user_interface.displayAllParks(coasters)
        elif user_choice.lower().strip() == "e":
            user_interface.displayCoastersInPark(coasters)
        elif user_choice.lower().strip() == "f":
            user_interface.findCoasters(coasters)
        elif user_choice.lower().strip() == "q":
            dummy +=2
main()