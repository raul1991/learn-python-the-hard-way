#Copy from one to another file

from sys import argv #for the arguments supplied
from os.path import exists

open(argv[2],'w').write(open(argv[1]).read())
script, from_file, to_file = argv

print "Copying from %s to %s" %(from_file, to_file)

#we could do these two on one line, how ?
f = open(from_file)
in_data = f.read()

print "The input file is %d bytes long" %len(in_data)

print "Does the output file exist?%r" % exists(to_file)

out_file = open(to_file, 'w')
out_file.write(in_data)

print "Alright, all done."

out_file.close()
f.close()
