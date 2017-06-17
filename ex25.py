# In order to import functions and use them do this:
# >>> import ex25
# You will be able to refer to functions like this:
# >>> ex25.break_words("Hello there Dasha")
# You will be also able to get documentation on ex25.py module by typing:
# >>> help(ex25)
# >>> help(ex25.break_words)

# This will import all functions from ex25.py and you can call functions without ex25.{function_name}
# >>> from ex25 import *
# >>> break_words("Hello there Dasha")

def break_words(stuff):
    # this is called documentation comments
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sort the words"""
    return sorted(words)

def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print word

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print word

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and the last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words, then prints the first and the last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
