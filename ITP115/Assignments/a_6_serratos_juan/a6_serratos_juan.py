   # Juan Serratos, jserrato@usc.edu
   # ITP 115, Fall 2022
   # Section: 31865
   # Assignment 6
   # Description: We create a program that asks the user to try to answer what correct word is given when presented with a scrambled up word.
def main ():
   import random 
   wrds = ["small", "universe", "code", "python"] # Creating a list so to scramble these word to ask the user for a guess 
   hints_wrds = ["alternate word for tiny", "the solar system is embedded into this thing", "computers read this as input", "known to be a relatively understandable coding language"] # Hints for each of the individual words in the list
   select = random.choice(wrds) # We pick a random word in our list of words
   select_hint = hints_wrds[wrds.index(select)] # We find the hint associated to the random word we just chose from 
   jumbled = list(select) # Creating a list containing each character from the random word we chose
   blah = '' # Our empty string that we use to scramble any given word in the list of words 
   for i in range (len(jumbled)): 
      x = random.choice(jumbled) # Choosing a random character in the list. 
      blah += x # Adding the character to our empty string, which will be our jumbled word in the end
      jumbled.remove(x) # Removing the character so that the character doesn't appear again in the final string.
   
   print("The jumbled word is " + '"' + blah + '"') # We begin asking the user to guess the scrambled word{ 
   guess = input("Enter your guess: ")
   if guess.lower() == select:
      print("You got it!") 
      print("It took you 1 guess.") # } (in the case they get it right the first around)
   else:
      count = 1 # we begin keeping track of how many attempts the user has tried to answer 
      print("That is not correct")
      while guess != select: # if the user guesses again incorrectly we up our count and ask if they would like a hint {
         count += 1
         hint = input(("Do you want a hint? (y or n) ")) 
         if hint.lower() == "y": # } if yes, then we print and see if they guessed correctly 
            print("Hint: " + select_hint)
            print("The jumbled word is " + '"' + blah + '"')
            guess_2 = input("Enter your guess: ")
            if guess_2.lower() == select:
               print("You got it!")
               print("It took " + str(count) + " attempts to guess the jumbled word.")
               guess = select
            else:
               print("That is not correct.") # if they guess wrongly and don't want a hint, then we begin again with another attempt { 
         else:
            print("The jumbled word is " + '"' + blah + '"')
            guess_3 = input("Enter your guess: ")
            if guess_3.lower() == select:
               print("You got it!")
               print("It took " + str(count) + " attempts to guess the jumbled word.")
               guess = select
            elif guess_3 != select:
               print("That is not correct") # } 
main()
