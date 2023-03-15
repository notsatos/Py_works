
   # Juan Serratos, jserrato@usc.edu
   # ITP 115, Fall 2022
   # Section: 31865
   # Assignment 4
   # Description: We create a while loop that takes in user input, multiple times, to calculate the mean of 
   # the collection of numbers for which the user inputs.

def main ():
    # # As step 14 says, we need to include a neccessary condition that repeats after the 
    # loop runs, so we start with that firstly {  
    step_14 = "y"
    string_1 = "Input an integer greater than or equal to 0 (or -1 to quit): "
    while step_14.lower() == "y": # }
        print(string_1)
        input_0 = int(input("> "))
        if input_0 !=-1 : # We will define necessary things if the user inputs the necessary input of not being -1 {
            count = 0
            sum = 0
            smallest_num = input_0
            largest_num = input_0 
            input_early = input_0 # } 
            while input_0 != -1:
                input_0 = int(input ("> "))
                if input_0 > largest_num: # We calculate the largest input by comparing to the first/previous input
                    largest_num = input_0
                if 0<= input_0 < smallest_num: # We calculate the smallest input by comparing to the first/previous input
                    smallest_num = input_0
                count += 1 # We keep track of how many times the while loop runs so we can calculate the mean, i.e. we divide by our count 
                sum += input_0 # We sum all user inputs so we can figure out the mean of the set of numbers... and then divide by our count
            largest_num_string = print("The largest number is:", largest_num)
            smallest_num_string = print("The smallest number is:", smallest_num)
            # print("Sum :", sum + input_early + 1) 
            # print("Count :", count)
            average_num_string = print("The average number is:", ( (sum + input_early + 1) /count ))
            step_14 = input("Would you like to enter another set of numbers (y/n)? ")
        else:
            step_14 = "n" # We quit our loop by forcing the outer loop to not be the required character of 'y'
    else:
        print("Goodbye!")
main()
