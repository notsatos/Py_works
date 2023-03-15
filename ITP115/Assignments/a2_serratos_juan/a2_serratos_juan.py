
   # Juan Serratos, jserrato@usc.edu
   # ITP 115, Fall 2022
   # Section: 31865
   # Assignment 2
   # Description: We generate a unique story according to unique inputs from a user using different parts of speech.
def main ():
    #Getting user input to begin generating a story using general aspects of language (nouns, verbs, and so on).
    noun = input("Give me a name of a fruit (plural): ")
    adjective = input("Give me a color for the fruit: ")
    verb_1 = input("Give me a verb ending in 'ing': ")
    verb_2 = input("Give me another verb, an activity: ")
    place = input("Give me the name of a city: ")


    #Getting more user input for aspects of the story that need numbers, and we perform a simple calculation 
    #that is going to used in our story.
    integer_1 = int(input("Enter a whole number greater than two: "))
    integer_2 = int(input("Enter another whole number greater than two: "))
    integer_3 = integer_1 + integer_2
    float_0 = float(input("Enter a real number: "))

    print("I found", "\""+ str(integer_1)+"\"", "\""+ noun +"\"", "in", "\""+ place +"\" earlier today.")
    print("I was ", "\""+ verb_1+"\"", "when I found the", "\""+ noun+"\"... it was a great thing that I found these", "\""+ noun+"\"." )
    print("They were", "\""+ adjective+"\"", "when I found them, but they turned brown when I went to go","\""+ verb_2+"\"." )
    print("With my luck, I will find", "\""+ str(integer_3) +"\"", "\""+noun +"\"","the next time I go", "\""+ verb_1+"\" if I spend", "\""+ str(float_0)+"\"", "more hours", "\""+ verb_1+"\".")
main()