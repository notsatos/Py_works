   # Juan Serratos, jserrato@usc.edu
   # ITP 115, Fall 2022
   # Section: 31865  
   # Lab 3
def main():
    string = "What would you like to know? \n a) Favorite Animal \n f) Favorite Food \n p) Favorite place \n q) Quit"
    print(string)
    info = input("> ")
    if info == "q" or info == "Q":
        info_1 = "q"
        print("Goodbye")
        quit()
    elif info == "a" or info == "A":
        info_1 = "a"
        print("This computer's favorite animal are wombats... they are native marsupials from Australia.")
    elif info == "f" or info == "F":
        info_1 = "f"
        print("This computer's favorite food is chicken tikka masala... which is considered to be indian food, yet this dish \noriginated in the United Kingdom.")
    elif info == "p" or info == "P":
        info_1 = "p"
        print("This computer's favorite place in the world is New York City in the United States.")
    else:
        info_1 = "z"
        print("That option is not available.")
    
    while info_1 != "q":
        print(string)
        new = input("> ")
        if new == "q" or new == "Q":
            print("Goodbye")
            quit()
        elif new == "a" or new == "A":
            print("This computer's favorite animal are wombats... they are native marsupials from Australia.")
        elif new == "f" or new == "F":
            print("This computer's favorite food is chicken tikka masala... which is considered to be indian food, yet this dish \noriginated in the United Kingdom.")
        elif new == "p" or new == "P":
            print("This computer's favorite place in the world is New York City in the United States.")
        else: 
            print("That option is not available.")

main()