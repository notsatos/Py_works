# Juan Serratos, jserrato@usc.edu
   # ITP 115, Fall 2022
   # Section: 31865  
   # Lab 5
import random


def main():
    nouns = ['Person', 'The Shah of Iran', 'The President']
    verbs = ['danced', 'moved', 'shifted']
    adverbs = ['angrily', 'happily', 'sadly', 'excitedly']
    stop = 0 
    while stop != 5: 
        print("Welcome to the Sentence Generator")
        print("1. View Words \n2. Add noun \n3. Remove Verb \n4. Generate Sentence \n5. Exit")
        input_1 = int(input("> "))
        if input_1 == 1:
            print("Nouns: " , nouns)
            print("Verbs: " , verbs)
            print("Adverbs:" , adverbs)
        elif input_1 == 2:
            new_word = input("Enter noun: ")
            nouns.append(new_word)
        elif input_1 == 3:
            remove_word = input("Pick word: ")
            if remove_word in verbs:
                verbs.remove(remove_word)
            else:
                print("Word is not in our verb list; Sentence Generator will restart.")
        elif input_1 == 4:
            noun = random.choice(nouns)
            verb = random.choice(verbs)
            adverb = random.choice(adverbs)
            print(noun, verb, adverb + ".")

        elif input_1 == 5:
            print("Thank you for using the Sentence Generator!")
            stop = 5
        else:
            print("Invalid choice.")
            stop = 5
main()