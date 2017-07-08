'''Write a program that asks the user for a Login Name and password.
Then when they type "lock", they need to type in their name and password to unlock the program.'''

from sys import exit

def unlock():
    print "Type your login"
    login = raw_input("> ")
    if login == login:
        print "There is a user with such login in the system. What's your password?"
        password1 = raw_input("> ")
        if password == password:
            print "Correct! Welcome in!"
        else:
            print "Password doesn't match login, sorry."

print "Please type your login:"
login = raw_input("> ")
print "Please type your password:"
password = raw_input("> ")

print "If you want to lock your computer just type 'lock'."
print "You will need your login and password to 'unlock' it later."

choice = raw_input("> ")

if choice == "lock":
    print "Your machine is locked."
    print "Do you want to unlock it?"
    choice = raw_input("> ")
    if choice == "yes":
        unlock()
    else:
        print "Okay, goodbye then."
else:
    print "Sorry, I don't know such command."
