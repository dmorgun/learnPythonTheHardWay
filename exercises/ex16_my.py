# close -- Closes the file. Like File->Save.. in your editor.
# read -- Reads the contents of the file. You can assign the result to a variable.
# readline -- Reads just one line of a text file.
# truncate -- Empties the file. Watch out if you care about the file.
# write('stuff') -- Writes "stuff" to the file.

from sys import argv
script, filename = argv

print "We're going to erase %r." % filename
print "If you don't wan't that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input ("?")

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."
input = ("%s\n%s\n%s\n") % (line1, line2, line3)
# print input
target.write (input)
target.close()

print "Let's see what's inside the file now: "
new_target = open(filename)
print new_target.read()

print "And finally, we close it."
new_target.close()
