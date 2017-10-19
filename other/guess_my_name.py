# Write a program that has a user guess your name, but they only get 3 chances to do so until the program quits.

name = "Daria"
guess = 0
count = 3

while guess != name and count > 0:
    guess = raw_input("What is my name? ")
    if guess != name and count > 0:
        count = count - 1
        if count > 0:
            print "No, it is not %s. You have %s more attempts to guess." % (guess, count)
        else:
            print "No, it is not %s. You have no more attempts to guess left." % guess
    elif guess != name and count == 0:
        print "Sorry, try again later."
#    elif guess == name:
#        print "Congrats! You won!"
    else:
        print "Congrats! You won!"
