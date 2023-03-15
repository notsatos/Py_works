   # Juan Serratos, jserrato@usc.edu
   # ITP 115, Fall 2022
   # Section: 31865
   # Assignment 7
   # Description: Functions
import random 
def displayRules(): 
   print("Let's play Rock Paper Scissors.\nThe rules of the game are:\n\tROCK smashes SCISSORS\n\tSCISSORS cut PAPER\n\tPAPER covers ROCK\n\tIf both the hands are the same, it's a tie")

def userPlays(optionList):
   rps = input("Enter ROCK, PAPER, or SCISSORS: ") 
   rps = rps.strip() # strip the user's input of unnecessary characters
   rps = rps.upper() # capitalize the input as that seems to be the convention for printing in this assignment
   while rps not in ["ROCK", "PAPER", "SCISSORS"]: # we ask the user for input until they input something valid 
      rps = input("Enter ROCK, PAPER, or SCISSORS: ")
      rps = rps.strip().upper() 
   print("User plays", rps)
   return rps # we take out the user's input for later use 

def computerPlays(optionList): 
   options = ["ROCK", "PAPER", "SCISSORS"] 
   computerOption = random.choice(options) # taking a random thing from the option's list to use against the user's input
   print("Computer plays", computerOption)
   return computerOption.upper() # making the computer's "input" upper case and returning it into our code for later use

def gameOutcome(computerStr, userStr): # for the game function, we will follow the simple rules of rock paper scissors and 
   # assign according values for the if statements given if the user beats the computer's random choice. 
   # In each case, we will return the value (-1 if the computer wins, 1 if the user wins, and 0 if there's a tie) to use later
   # in the main function to count how many times each has won. 
   if computerStr == userStr: 
      print("You and the computer tied")
      value_cpu = 0
      return value_cpu
   elif userStr == "PAPER" and computerStr == "ROCK":
      print ("You win!")
      value_usr = 1
      return value_usr 
   elif userStr == "ROCK" and computerStr == "PAPER":
      print("Computer wins")
      value_cpu = -1 
      return value_cpu 
   elif userStr == "PAPER" and computerStr == "SCISSORS":
      print("Computer wins")
      value_cpu = -1
      return value_cpu 
   elif userStr == "ROCK" and computerStr == "SCISSORS":
      print("You win")
      value_usr = 1
      return value_usr
   else:
      print("Computer wins")
      value_cpu = -1
      return value_cpu
      
def main():
   count_usr = 0 # to keep track of how many times the user has won
   count_cpu = 0 # to keep track of how many times the computer has won
   optionList = ["ROCK", "PAPER", "SCISSORS"] # the optionList as described in the instructions
   displayRules()
   while count_usr < 2 and count_cpu < 2: # we allow for the while loop to keep going only if the amount of times the user and computer have won are less than two times respectively
      usr_option = userPlays(optionList) # take in the user's input
      cpu_option = computerPlays(optionList) # computer chooses a random item from ["ROCK", "PAPER", "SCISSORS"] 
      game = gameOutcome(cpu_option, usr_option) # execute the game 
      if game == -1: # this is if the computer wins; we keep track as to how many times
         count_cpu +=1
      elif game == 1: # this is if the user wins; we keep track as to how many times
         count_usr +=1
      if count_usr == 2: # we terminate once the user has won two games
         print("You won 2 games!")
      elif count_cpu == 2: # or we terminate once the computer has won twice... whichever comes first.
         print("The computer has won 2 games.")
main()
