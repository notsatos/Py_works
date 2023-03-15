# Juan Serratos, jserrato@usc.edu
# ITP 115, Fall 2022
# Section: 31865
# Final Project
# helper.py
# Description: We write a program that manages/creates a menu for the user to play with.
# THERE IS AN ERROR WITH MY COMPUTER/PYTHON THAT DOESN'T SEEM TO SEE THE COASTER.CSV IN THE SAME FOLDER SO 
# IT NEEDS A MORE DESCRIPTIVE PATH. PLEASE CHANGE TO NORMAL "roller_coasters.csv"  WHEN GRADING.
import user_interface
import helper

def createCoastersFromFile(filenameStr = "/Users/kafka/Desktop/ITP115/project_serratos_juan/roller_coasters.csv"):
    # we open the file up, read it, and get the top labels/header (e.g. name,material type,seating type, etc...)
    fileIn = open (filenameStr, "r")
    Zar = fileIn.readline().strip().split(",")
    # we make an empty list to add data later on
    list_0 = [ ]
    # in the following algorithm, we check to see whether or not what 
    # information we're sourcing has extra commas
    for j in fileIn:
        if len(j)>len(Zar):
            j=j.split(",")
            j[len(Zar)-1]=','.join(j[len(Zar)-1::])
        Zar_diction = { }
        dummy = 0 
        for x in Zar:
            Zar_diction[x] = j[dummy].strip().replace('"','')
            dummy+=1
        list_0.append(Zar_diction)
    fileIn.close()
    # we lastly add the dictionary to our list and close our file, and we return this initally empty list
    return list_0 
def getFastestCoaster(coastersList):
    small = -1 
    # we fix a small value to check compare against all other speeds 
    # so that can keep looking at other coasters to find the one with the highest speed
    dict = { }
    name = "name"
    dict [name] = 0
    # for the thing in coastersList 
    # we first check that we have a digit rather than an empty string 
    for x in coastersList:
        if x["speed"].isdigit() == True:
            # after that we assign size to be the speed of the current coaster 
            size=float(x["speed"])
            # if the new size is greater than the last then we make this 
            # our new small size
            if size > small :
                small =float(x["speed"])
                code = x["name"]
            dict[name] = code 
    return dict # we finally return the dictionary with the fastest coaster
def getParksList(coastersList):
    # we make an empty list 
    lis = [ ]
    # for every coaster in coasterList, we add the name of the coaster to 
    # the empty list and finally sort it and return it to the user.
    for x in coastersList:
        name = x["park"]
        if name not in lis:
            lis.append(name)  
    lis.sort()
    return lis 
