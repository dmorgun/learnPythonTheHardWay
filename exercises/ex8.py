formatter = "%r %r %r %r"
# Printing the sequence of numbers
print formatter % (1, 2, 3, 4)
# Printing 4 small strings with numbers
print formatter % ("one", "two", "three", "four")
# Printing boolean values
print formatter % (True, False, False, True)
# Printing formatter 4 times
print formatter % (formatter, formatter, formatter, formatter)
# Printing 4 lines of text into 1 line
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)
