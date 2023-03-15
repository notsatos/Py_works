   # Juan Serratos, jserrato@usc.edu
   # ITP 115, Fall 2022
   # Section: 31865
   # Assignment 5
   # Description: We create a program to ask the user (string) input to see how many special characters
   # are included in their input, and we also check the alphabet distrbution in the input, i.e. find how many
   # times an alphabetical letter appears in the input.


def main ():
   alph = "abcdefghijklmnopqrstuvwxyz" # Our alphabet string 
   loop_times = int(input("Times do you want to loop: ")) # We ask the user how many times they want to loop premptively. 
   for i in range(loop_times):
      input_0 = input("Enter a sentence: ")
      count = 0
      for ltr in input_0: # We loop through the characters in the user's input string.
         if ltr.lower() not in alph and ltr != " ": # Specifically taking the lower verison of the letter, so as not to matter about capitalization or not.
            count += 1 # If the users input is not in alph, then it is a special character, and so we keep track of how many special characters there are. 

      if count > 0: # Establishing how many special characters, if any { 
         print("Special Characters: " + "*" * count)
      else:
         print("Special Characters: " + "NONE") # } 

      for ltr in alph: # The loop we can use to find out the alphabet distribution in the user's string: { 
         count_2 = 0 
         if ltr in input_0.lower(): # We check if the character is in the user's string 
            for i in input_0: # We use a nested loop to take into account multiple instances of a character in the string appearing
               if ltr == i.lower():
                  count_2 += 1 # }

         if count_2 > 0: # Establishing the alphabet distrbution {
            print(ltr + ": " + "*" * count_2)
         else:
            print(ltr + ": NONE") # }
main()
