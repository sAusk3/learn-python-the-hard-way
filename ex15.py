from sys import argv
#imports the module argv from sys

script, filename = argv
#unpacks the argument containing the scripename and the file name to be read

txt = open(filename)
#returns the file by opening it

print "Here's your file %r:" % filename
print txt.read()
#reads the content of the file and prints it

print "Type the filename again: "
file_again = raw_input('> ')

txt_again = open(file_again)

print txt_again.read()
