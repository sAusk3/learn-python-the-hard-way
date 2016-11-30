from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %r to %r" %(from_file, to_file)

#we could do thses two on one line, how ?
#in_file = open(from_file)
indata = open(from_file).read()

#print "the input file is %d bytes long" % len(indata)

#print "Does the output file exist? %r" % exists(to_file)
#print "Hit enter to continue, Ctrl-C to abort."
#raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

#print "Alright! All done."

out_file.close()
#in_file.close()
