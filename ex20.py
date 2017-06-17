# Importing argv module
from sys import argv

# Describing arguments that should be passed when running a file
script, input_file = argv

# Define fucntion to print all content of a file
def print_all(f):
    print f.read()

# Define function to rewind to the beginning of a file
def rewind(f):
    f.seek(0)

# Define function to print a single line of a file
def print_a_line(line_count, f):
    print line_count, f.readline()

# Open file
current_file = open(input_file)

print "First let's print the whole file:\n"
print_all(current_file)

print "Now let's rewind, kind of like a tape."
rewind(current_file)

print "Let's print 3 lines:"

current_line = 1
print_a_line(current_line, current_file)

# The expression with '+=' below is equal to 'current_line = current_line + 1'
current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)
