# Juan Serratos, jserrato@usc.edu
   # ITP 115, Fall 2022
   # Section: 31865  
   # Lab 9
   # PLEASE CHANGE FILE NAME IN MAIN() — MY PYTHON PATH DOESN'T WORK PROPERLY SO I HAVE TO BE VERY SPECIFIC ABOUT 
   # THE NAME OF THE FILE BY INCLUDING THE MOST ACCURATE PATH

def readFile(fileName):
    fileIn = open(fileName, "r")
    alph = "abcdefghijklmnopqrstuvwxyz"
    alph = alph.strip()
    diction = {}
    for x in fileIn:
      for j in x:
         if j.lower() in alph:
            if j.lower() in diction.keys():
               diction [j.lower()] += 1
            elif j.lower() not in diction.keys():
               diction [j.lower()] = 1
      fileIn.close()
      return diction
def sortKeys(dictionary):
   initial_list = list(dictionary.keys())
   new_list = sorted(initial_list)
   return new_list

def main():
   fileNam = "/Users/kafka/Desktop/ITP115/Labs/lab_9_serratos_juan/speech.txt"
   newreadFile = readFile(fileNam)
   newKey = sortKeys(newreadFile)
   for x in newKey:
      print(x + ": " + str(newreadFile[x]))
main()

