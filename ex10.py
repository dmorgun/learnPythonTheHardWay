print "I am 6'2\" tall" # escape double-quote inside the string
print 'I am 6\'2" tall' # escape single-quote inside the string

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip \n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

print "Hey ASCII bell \a hey"
print "Hey ASCII backspace \b hey"
print "Hey ASCII formfeed \f hey"
print "Hey ASCII linefeed \n hey"
print "Hey Character named name in the Unicode database (Unicode only) \N{B}"
print "Hey Carriage Return\r bobo"
print "\v It's a vertical \v tab"
print "Hey Horizontal Tab \t hey"

while True:
    for i  in ["/", "-", "|", "\\", "|"]:
        print "%s\r" % i,
