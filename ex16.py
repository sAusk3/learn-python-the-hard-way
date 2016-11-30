from sys import argv

script, filename = argv

print "We are going to erase %r." % filename
print "If you don't want that , hit ctrl+C (^c)."
print "If you don't want that, hit enter"

raw_input("?")

print "Opening the file...."
target = open(filename, 'w')

print "truncating the file. Goodbye!"
target.truncate()

print "Now I am going to ask for three lines"

line1 = raw_input("Line 1: ")
line2 = raw_input("Line 2: ")
line3 = raw_input("Line 3: ")

print "I'm going to write these to the file."

target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")

print "And finally, we close it."
target.close()