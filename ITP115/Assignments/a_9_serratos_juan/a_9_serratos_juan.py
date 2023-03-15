# Juan Serratos, jserrato@usc.edu
# ITP 115, Fall 2022
# Section: 31865
# Assignment 9
# Description: We translate some words/input from the user to different languages using files and functions. THERE IS AN ISSUE 
# WITH MY PYTHON WHICH DOESN'T CORRECTLY READ THE PATH FOR MY ASSIGNMENT, SO I NEEDED TO EXPLICITY STATE THE PATH IN MY CODE
# RATHER THAN JUST WRITING "languages.csv".

# First we define a function that will read our language.csv's heading in a nice way (stripping) and return it a list
def readFileForLanguages(filenameStr):
    fileIn = open(filenameStr, "r")
    s1 = fileIn.readline().strip()
    fileIn.close()
    return s1.split(",")

def getLanguageFromUser(languagesList):
  # We use our previous function to a generate a local list that will not include English.
  lang_0 = readFileForLanguages("languages.csv")
  for line in lang_0:
    if line == 'English':
        lang_0.remove(line)
  print("Translate English words to one of the following languages", lang_0)

  # To check lowercase instances we make a new list in terms of lower cases to make our lives easier
  # to check whether or not an object is in our list.
  lang_1 = []
  for item in lang_0:
    n = item.lower().strip()
    lang_1.append(n)
  langchoice = input("Enter a language: ")
  # we make a while loop to make sure we get valid input from the user
  while langchoice.lower().strip() not in lang_1:
    langchoice = input("Enter a language:")
    langchoice.lower().strip()
  print("You have entered", langchoice.strip().capitalize())
  return langchoice.strip().capitalize() # we return a stripped and capitalized list to be used later on


def readFileForWords(filenameStr, languagesList, languageStr):
    initial_list = [] # we make an empty list so we can later append things needed to it
    fileIn = open(filenameStr, "r") 
    fileIn.readline() # we're looking at again the top row of our file that we're reading
    x = languagesList.index(languageStr) # We are determining the index of the language and appending the correct word to our list
    for line in fileIn:
        lineList = line.split(",")
        initial_list.append(lineList[x])
    fileIn.close() # lastly we close the file, 
    return initial_list # and return to allow us to use this list later

def createFileWithTranslations(languageStr, englishList, translationList):
  newFile = languageStr + ".txt" # We make a new file of the given language which will have of the words the user decides to translate and 
  newFileIn = open(newFile, "w") # so we write to the file.
  print("Words translated from English to", languageStr, file = newFileIn)
  j = 0 # we make a dummy intial condition to make sure we're getting valid input from the user
  while j == 0:
    trns = input("Enter a word to translate (return to quit): ")
    trns = trns.lower().strip()
    if trns in englishList: # we check whether or not we can translate the user's word given our list
      engindex = englishList.index(trns) # we attempt to identify the word's index place
      if translationList[engindex] == "-":
        print(trns, "has no translation in this program.") # we there's no index place then we cannot translate
      else: 
        trns_exist = translationList[engindex] # if the word exsits in our list 
        print(trns + " translates to", trns_exist) # then we translate it produce the corresponding input giving the user the translated word and
        print(trns + " ->", trns_exist, file =newFileIn) # also implenting it into the file we're writing to.
    elif trns not in englishList and trns != " " and trns !="": # lastly we check some basic cases to make sure we keep 
      print(trns + " is not in the English list.") # looping even if we're getting invalid input
    if trns == " " or trns =="": # this if statement will decide whether or not we keep running the while loop
      j+=1
    else: 
      j=0
  print("Translated words have been saved to", languageStr + ".txt") # We are then done and print and 
  newFileIn.close() # close the file. 


def main():
  print("Language Translator")
  csvName = "/Users/kafka/Desktop/ITP115/Assignments/a_9_serratos_juan/languages.csv"
  return_language_list = readFileForLanguages(csvName)
  return_read_file = readFileForWords(csvName, return_language_list, "English")
  language_choice = getLanguageFromUser(return_read_file)
  file_for_word = readFileForWords(csvName, return_language_list, language_choice)
  createFileWithTranslations(language_choice,return_read_file,file_for_word)
main()
