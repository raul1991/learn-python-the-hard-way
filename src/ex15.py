"""
Title : Reading from a file in python
-----
Description :
-----------
Open an already existing file, and print
its contents.

Names
-----
ex15.py, ex15_sample.txt

Contents
--------
This is stuff I typed into a file.
It is really cool stuff.
Lots and lots of fun to have in here.
"""

#load the sub-module named argv(argument variable) from the module sys
from sys import argv

#unpacking the arguments into variables
script, filename = argv

#get the file using the filename as argument
txt = open(filename)

print "Here's your file %r:" %filename
#read from the file and print on the console.
print txt.read()
txt.close()
print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)
#read from the file
print txt_again.read()
txt_again.close()
