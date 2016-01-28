from sys import argv

script, filename = argv

print "We're going to create %r." %filename
print "If you don't want that, hit CTRL-C (^C)"
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
target.truncate()

print "Now i'm going to ask you for three lines"

title = raw_input("line 1: ")
description = raw_input("line 2: ")
notes = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write(title+"\n"+description+"\n"+notes)

print "And finally, we close it."
target.close()
