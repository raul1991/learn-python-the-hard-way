from sys import argv

wish, first, second = argv
print "Welcome to the wishing well..."
print "Make a wish:", wish
print "Once more, what was it:", first 
print "Almost done, say it once more and close your eyes:", second
print "That ain't gonna happen.So long... mate"

#drill
count = -1
while count != 3:
   count = int(raw_input("How many wishes do you want?"))
   if count == -1 or count == 0 :
      print "Noooooo, You sound so low, come on ask for more."		
   elif count > 3 :
      print "Nope!!!Not so many"
   elif count < 3:
      print "Don't be modest, ask for more."
print "We are super busy right now...See you next year on christmas with your wishes..."

