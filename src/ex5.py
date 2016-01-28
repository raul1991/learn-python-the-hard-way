my_name = 'Rahul Bawa'
my_age = 35 #not a lie
my_height = 74
my_weight = 180
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print "Let's talk about %s." %my_name
print "He's %d inches tall." %my_height ,"or %d centimeters" %(my_height * 2.54)
print "He's %d pound heavy." %my_weight ,"or %d kilograms"  %(my_weight/.45)
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." %(my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." %my_teeth

#this line is tricky, try to get it exactly right
print "If I add %d, %d and %d I get %d" % (my_age ,my_height, my_weight, my_age + my_height + my_weight)

#Drills - testing some more formatting options.
print "Contains decimal %f" %(0.5)

