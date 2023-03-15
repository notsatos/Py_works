   # Juan Serratos, jserrato@usc.edu
   # ITP 115, Fall 2022
   # Section: 31865
   # Lab 8
def readFile(userGenre, fileName):
   intial_list = []
   fileIn = open(fileName, "r")
   for line in fileIn:
      name, genre = line.strip().split(",")
      if userGenre in genre:
         intial_list.append(name)
   fileIn.close()
   return intial_list

def writeFile(genre, showList):
   inputFile = open(genre + ".txt", "w")
   Ne = "\n".join(showList)
   print(Ne, file = inputFile)
   inputFile.close()

def main():
   print("TV Shows")
   phrase = print("Possible genres are action & adventure, animation, comedy, documentary, drama, mystery & suspense, science fiction & fantasy")
   liszt = ["action & adventure", "animation", "comedy", "documentary", "drama", "mystery & suspense", "science fiction & fantasy"]
   usrInput = input("Enter a genre: ")
   while usrInput not in liszt:
      usrInput = input("Enter a genre: ")
   N = readFile(usrInput, "shows.csv")
   writeFile(usrInput, N)
   print("The file " +"'"+ usrInput+".txt"+"'"+" has the following shows:" )
   print(N)
main()