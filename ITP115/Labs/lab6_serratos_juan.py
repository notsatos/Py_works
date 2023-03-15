# Juan Serratos, jserrato@usc.edu
   # ITP 115, Fall 2022
   # Section: 31865  
   # Lab 6

def printRectangle (length, width):
    print(" " + "-"*width)  
    for line in range(length):
        print("|" + " " * width + "|")
    print(" " + "-" * width) 

def printSquare(side):
    print(" " + "-" * side)  
    for i in range(side):
        print("|" + " " * side + "|")
    print(" " + "-" * side) 

    
def main():
    print("What would you like to print?")
    print("r) rectangle")
    print("s) square")
    shapeUser = input("> ")
    if shapeUser.lower() == "r":
        lengthUser = int(input("Enter the length: "))
        widthUser = int(input("Enter the width: "))
        printRectangle(lengthUser, widthUser)
    elif shapeUser.lower() == "s":
        sideUser = int( input("Enter the side: "))
        printSquare(sideUser)
    else:
        print("That shape is not supported.") 
main()