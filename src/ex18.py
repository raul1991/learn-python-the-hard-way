"""
Title : Introduction to the functions
-----
They name pieces of code the way variables name strings and numbers.
They take arguments(something , some variables to work on)
Create a function using the reserved keyword in python ie : def

Description :
-----------
Create four functions named print_two, print_two_again,print_one,print_none
"""

#this one is like your scripts with argv
def print_two(*args):
   arg1,arg2 = args
   print "arg1: %r, arg2: %r" % (arg1, arg2)

def print_more(arg2,*args):
   print args[0],arg2

#takes two arguments
def print_two_again(arg1,arg2):
   print "arg1: %r, arg2: %r" %(arg1, arg2)

#takes one argument
def print_one(arg1):
   print "arg1: %r" %arg1

#this one takes no args
def print_none():
   print "I got nothin'."

print_two("Rahul","Bawa")
print_more("Glad it worked.","School","is","What","is","missing")
print_none()
print_one("Just me")
print_two_again("Rahul","Bradshaw")
