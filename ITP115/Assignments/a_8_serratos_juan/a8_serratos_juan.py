# Juan Serratos, jserrato@usc.edu
# ITP 115, Fall 2022
# Section: 31865
# Assignment 7
# Description: We create a program where the user attempts to guess a randomly generated list containing three digits.
import random
digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# This is how we will check if the user is proving valid input;
# the input is only valid they provide us with some digits and the length of the string is 1.
def isSingleDigit(userStr):
  if len(userStr) == 1 and int(userStr) in digits:
    return True
  else:
    return False
# This will be our "secret" list/code that the user will be attempting to guess throughout the program.
# We take an empty list and simply append/add to it random digits from 0 through 9.
def generateCodeList(size):
  random_list = []
  for i in range(size):
    random_num = random.randint(0, 9)
    random_list.append(random_num)
  return random_list
# We start with an empty list, then start appending the user's input/guesses as to what the secret list is and 
# we do some checking using our isSingleDigit to check whether or not the user's input is valid, and additionally we create a while loop
# as we want to get three digits of user input to see whether or not if it lines up with the randomly generated list (the secret list/code). Once
# we've taken in enough valid input, we end the loop (in a somewhat gross way).
def getUserList(size):
  intial_list = []
  print("The number of digits in the code is " + str (size))
  for i in range(size):
    holder = 1
    while holder == 1:
      usr_input = input("Enter a digit at index " + str(i) + ": ")
      if isSingleDigit(usr_input):
        intial_list.append(int(usr_input))
        holder += 1
  print("Your guess is", intial_list)
  return intial_list
# Firstly, we look at our secret list and compare to the user's list/three guesses made and see if any of the digits they inputted 
# line up and count how many times that corresponding digits appears. Moreover, we check with the second for loop to see if any of the 
# digit places from the user's list and secret list line up. These are our hints.
def printHints(codeList, userList):
  print("Generating hints...")
  count = 0
  for i in userList:
    if codeList.count(i) >= 1:
      count += 1
      print(str(i) + " appears", codeList.count(i), " many times.")
  for j in range(len(codeList)):
    if userList[j] == codeList[j]:
      print(codeList[j], "is in the correct position")
  if count == 0:
    print("No hints were given.")
# In our main output, we decide on always having a secret list of length three and create a while loop to begin comparing
# against the user list; ultimately, the user will guess until both lists line up with having the same digits in the same places.
# We count how many guesses it takes as well and print that.
def main():
    sz = 3
    liszt = []
    secret_code = generateCodeList(sz)
    count = 0
    while liszt != secret_code:
        count += 1
        liszt = getUserList(sz)
        printHints(secret_code, liszt)
    print("You cracked the code in", count, "guesses!")
main()