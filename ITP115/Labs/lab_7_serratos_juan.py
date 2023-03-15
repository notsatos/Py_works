# Juan Serratos, jserrato@usc.edu
   # ITP 115, Fall 2022
   # Section: 31865  
   # Lab 7
import random
def coin ():
    toss = random.choice(["heads", "tails"])
    return toss
def experiment():
    count = 0
    count_heads = 0 
    while count_heads < 3:
        flip = coin()
        if flip == "heads":
            count += 1
            count_heads += 1
        elif flip == "tails":
            count += 1
            count_heads = 0
    return count
def main():
    count_flips = 0
    for x in range (10):
        count_flips += experiment()
    print("The average for 3 heads in row is:", (count_flips/10))
main()