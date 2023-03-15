   # Juan Serratos, jserrato@usc.edu
   # ITP 115, Fall 2022
   # Section: 31865  
   # Lab 2
def main():

   year = int(input("Enter a year: "))
   x = year % 12

   if x == 0:
      print(str(year), "is the Year of the Monkey.")
   if x == 1:
      print(str(year), "is the Year of the Roost.")
   if x == 2:
      print(str(year), "is the Year of the Dog.")
   if x == 3:
      print(str(year), "is the Year of the Pig.")
   if x == 4:
      print(str(year), "is the Year of the Rat.")
   if x == 5:
      print(str(year), "is the Year of the Ox.")
   if x == 6:
      print(str(year), "is the Year of the Tiger.")
   if x == 7:
      print(str(year), "is the Year of the Rabbit.")
   if x == 8:
      print(str(year), "is the Year of the Dragon.")
   if x == 9:
      print(str(year), "is the Year of the Snake.")
   if x == 10:
      print(str(year), "is the Year of the Horse.")
   if x == 11:
      print(str(year), "is the Year of the Goat.")

main()