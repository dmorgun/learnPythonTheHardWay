# Import argv system module
from sys import argv

# Define what parameter(s) should be requested from user as he run the python script.
# In this example it's 1 parameter 'filename'
script, filename = argv

# Open a file and save file object to variable 'txt'
txt = open(filename)

# Print file name
print "Here's your file %r:" % filename
# Print file contents
print txt.read()
# Close file
txt.close()

# Request file name from user once again via raw_input
print "Type the filename again:"
file_again = raw_input("> ")

# Open a file again and save file object to variable 'txt_again'
txt_again = open(file_again)

# Print file contents
print txt_again.read()
# Close file
txt_again.close()
