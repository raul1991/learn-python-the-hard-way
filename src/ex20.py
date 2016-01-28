"""
Title : Functions and files
-----

Description :
-----------
Let's see how functions and files work together.

"""

from sys import argv

script, input_file = argv

"""
prints all at once.
"""

def print_all(f):
   print f.read()

"""
Takes the file pointer(point where read or any other read function
would start reading from) to the first step.
"""
def rewind(f):
   f.seek(0)

"""
prints line by line of the file f
"""
def print_a_line(line_count, f):
   print line_count, f.readline()

current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
