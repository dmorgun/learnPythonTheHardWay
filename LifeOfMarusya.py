from sys import exit

# Marusya's mood can be in (-2, -1, 0 , 1, 2), where -2 is a very sad mood, -1 is sad,
# 0 is neutral, 1 is good, 2 is happy
mood = 0

# TODO: Game intro

def finish(why):
    print why, "See you next time, Marusya!"
    exit(0)

def purr():
    print "You start purring with deep pleasure."
    print "Life is good, so why not purr?"
    global mood
    if mood < 1:
        mood += 1
    else:
        # TODO
        print ""
    raw_input("Next...")

#purr()

def meow():
    print "You start meowing for no obvious reason."
    raw_input("Next...")
    print "Actually you're sending the signal to the outer space in search of other forms of life."
    raw_input("Next...")
    print "Noone ever sent you a signal back. Yet."
    raw_input("Next...")
    print "Whoops! Your human throws a pillow at you! Poor bastard."
    global mood
    mood -= 1
    print mood

# meow ()

def sleep():
    print "Your energy slowly fades and you feel that you need some rest."
    raw_input("Next...")
    print "You find a cozy corner on the sofa and curl up, covering your nose with the tip of your tail."
    raw_input("Next...")
    print "Soft kitty, warm kitty, little ball of fur..."
    raw_input("Next...")
    print "Happy kitty, sleepy kitty, purr, purr, purr..."
    global mood
    mood += 1

# sleep()

def watch_birds():
    print "Suddenly you hear nasty pigeons mocking at you from the outside."
    raw_input("Next...")
    print "All right! That's it! Time for a furrrious revenge!!!"
    raw_input("Next...")
    print "What are you gonna do to teach those bastards a lesson?"
    print "1. Lurk and scare"
    print "2. Ignore"
    print "3. Kill"
    choice = raw_input("---> ")
    choice.lower()
    print choice
    if choice in ("1", "lurk", "scare"):
        print "You lie down and hide from the birds sight and then quickly jump from behind with dreadful MEOW!"
        raw_input("Next...")
        print "Pigeons were not expecting that! They crap thier pants and run away ignominiously!"
        global mood
        mood += 1
    elif choice in ("2", "ignore"):
        print "After a few seconds you realize that they're not worth it. Ignorance is the best weapon."
    elif choice in ("3", "kill"):
        print "You gallop towards the balcony, ready to catch and defeat!"
        raw_input("Next...")
        print "But somewhere along the way you slip on the wet floor and miss the hit."
        raw_input("")
        print "Pigeons gaggle at your clumsiness, you feel defeated."
    else:
        print "Your answer should have be 1, 2 or 3. Start over"
        watch_birds()

# watch_birds()

def eat():
    print "You start feeling a bit hungry. Time to grab some food."
    print "You go check your food bowl and it's empty!"
    print "Your human seems to be sleeping on the couch."
    print "How are you gonna wake her up?"
    print "Available options: meow, sleep, purr."
    human_asleep = True
    second_try = False

    while True:
        choice = raw_input("--->")
        if choice in ("meow") and second_try:
            finish("Your human gets angry at you making loud meowy noises and throws a pillow at you!")
        elif choice in ("meow") and not second_try:
            second_try = True
            print "Can't she hear you starving or what?"
        elif choice in ("sleep") and not second_try:
            print "You decide to take a nap and curl up by your human's side."
            second_try = True
        elif choice in ("sleep") and second_try:
            print "You dream of juicy meatballs and fresh salmon steaks."
        elif choice in ("purr") and human_asleep:
            purr()
            human_asleep = False
            print "But your human seems to be still sleeping. What do you do?"
        elif choice in ("purr") and not human_asleep:
            print "Well that strategy seems to work out. Your human wakes up and feeds you. Nice!"
            global mood
            mood += 1
            play()
        else:
            finish("That didn't help. Game over.")

def play():
    print "You feel a boost of energy."

# TODO: def play
"""1. Play hide-and-seek - eat
2. Chase your tail - sleep
3. Hunt your human - purr"""
