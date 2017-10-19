substring = raw_input("Type a substring to look for:")
print "The substring to look for is '%s.''" % substring
lowercase_substring = substring.lower()
print lowercase_substring
text = raw_input("Type a text in which Python would look for a substring:")
lowercase_text = text.lower()
# print lowercase_text
print "The substring was found in the text %d times." % lowercase_text.count(lowercase_substring)
