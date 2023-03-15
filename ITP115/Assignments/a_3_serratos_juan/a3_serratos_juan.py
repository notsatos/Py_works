
   # Juan Serratos, jserrato@usc.edu
   # ITP 115, Fall 2022
   # Section: 31865
   # Assignment 3
   # Description: We code a vending machine based on the Harry Potter currency where the user has the choice of four
   # options and we calculate conversions of the Harry Potter currenices to produce valid outputs to the user.

def main ():
    # Here we ask the user what they want from the vending machine and we also account for the difference if capitalization, e.g.
    # if the user enters "b" or "B" then they are treated the same. We also define what the cost of an item in terms of knuts repsective to what they are defined to be in 
    # the homework pdf/instructions. 
    print("Please select an item from the vending machine: \n  a) Assortment of Candy for 11 sickles and 7 knuts  \n  b) Butterbeer for 2 sickles \n  c) Quill for 6 sickles \n  d) Daily Prophet for 5 knuts ")
    choice = input("Enter choice: ")
    if choice == "B" or choice == "b":
        choice = "b"
        choice_string = "Butterbeer for 2 sickles"
        cost_sickles = 2
        cost_knuts = 0
        cost = 29 * cost_sickles + cost_knuts
        item_name = "Butterbeer"
    elif choice == "A" or choice == "a":
        choice = "a"
        choice_string = "Assortment of Candy for 11 sickles and 7 knuts"
        cost_sickles = 11
        cost_knuts = 7
        cost = 29 * cost_sickles + cost_knuts
        item_name = "Assortment of Candy" 
    elif choice == "C" or choice == "c":
        choice = "c"
        choice_string = "Quill for 6 sickles "
        cost_sickles = 6
        cost_knuts = 0
        cost = 29 * cost_sickles + cost_knuts 
        item_name = "Quill"
    elif choice == "D" or choice == "d":
        choice = "d"
        choice_string = "Daily Prophet for 5 knuts"
        cost_sickles = 0
        cost_knuts = 5
        cost = 29 * cost_sickles + cost_knuts
        item_name = "Daily Prophet" 
    else:
        print("Error: You have chosen an invalid choice, your choice is Quill as default.")
        choice = "c"
        choice_string = "Quill for 6 sickles "
        cost_sickles = 6
        cost_knuts = 0
        cost = 29 * cost_sickles + cost_knuts
    
    # We ask the user how much currency in each option (Galleons, Sickles, and Knuts) they are going to enter and store their values in 
    # the following respective variables. 
    print("Please pay by entering the number of each coin ")
    galleons = int(input("Number of galleons: "))
    sickles = int (input("Number of sickles: "))
    knuts = int (input("Number of knuts: "))

    # We calculate the input of currencies in terms of knuts and add the total to keep an active wallet to use for the user's purchases. 
    wallet_galleons = 493 * galleons 
    wallet_sickles = 29 * sickles 
    wallet_knuts = 1 * knuts
    total_wallet = wallet_galleons + wallet_sickles + wallet_knuts

    print(str(wallet_knuts), str(wallet_sickles), str(wallet_galleons) )
    print("Total knuts:", total_wallet)
    print("Cost in knuts:", cost)
    print("Payment in knuts: ", total_wallet)

    if total_wallet < cost:
        print("You did not enter enough money and will not receive the",  item_name)
        # you can add "quit()" here to make the output of the code cleaner and not showing the 
        # errors that run beyond this condition being true, but this has not been shown in lecture.
    else:
        difference = total_wallet - cost
        difference_gal = difference // 493
        leftover_gal = difference % 493 

        difference_sick = leftover_gal // 29
        leftover_sick = leftover_gal % 29

        difference_knuts = leftover_sick // 1 
  

        print("You purchased", item_name)
        print("Your change is", str(difference), "knuts.")
        print("In terms of galleons, sickles, and knuts:")
        print("Galleons:", difference_gal)
        print("Sickles:", difference_sick)
        print("Knuts:", difference_knuts)
    

main()