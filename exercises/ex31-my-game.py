print "What is your name?"
name = raw_input("> ")

print "Hello %s, what is your mood today?" % name
print "1. Happy"
print "2. Sad"
print "3. Average"

mood = raw_input("> ")

if mood == "1":
    print "I'm very happy for you, %s. Keep doing whatever you're doing." % name
elif mood == "2" or mood == "3":
    print "That's too bad. Let's try to cheer you up."
    print """Try to do one of these:
    1. Eat some candy
    2. Smile without any reason
    3. Watch video with kitties"""
    print "What is your choice?"

    choice = raw_input("> ")

    if choice == '1':
        print "Don't forget to exercise!"
    elif choice == '2':
        print "Feels better now, huh?"
    elif choice == 'fuf3':
        print "Aren't they cute?!"
else:
    print "Sorry, I don't understand. Please try answering 1, 2 or 3."
