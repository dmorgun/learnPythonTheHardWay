# -*- coding: utf-8 -*-
# encoding: utf-16

from sys import exit

# Marusya's mood can be in (-2, -1, 0 , 1, 2), where -2 is a very sad mood, -1 is sad,
# 0 is neutral, 1 is good, 2 is happy
mood = 0

# TODO: Game intro
def start():
    print "Have you ever wondered what it's like to be a cat?"
    raw_input("Next...")
    print "Well, you can be one now!"
    raw_input("Next...")
    print "You're a supercat named Marusya."
    raw_input("Next...")
    print "You're undercover, so don't let your human get too suspicious."
    raw_input("Next...")
    print "Your mission is to live through the day."
    raw_input("Next...")
    print "Let the journey begin!"
    print "\n(=^･ｪ･^=))ﾉ彡☆"
    raw_input("Next...")
    print "...................................................................."
    print "...This is your single day at your home in the middle of Chaiky..."
    print "...................................................................."
    raw_input("Next...")

def finish(why):
    print why
    print "(=✖.✖=)"
    print "See you next time, Marusya!"
    exit(0)

def purr():
    print "You start purring with deep pleasure."
    raw_input("Next...")
    print "Life is good, so why not purr?"
    #global mood
    #if mood < 1:
    #    mood += 1
    #else:
        # TODO
        #print ""
    raw_input("Next...")

#purr()

def meow():
    print "You start meowing stridently."
    raw_input("Next...")
    print "Actually you're sending the signal to the outer space in search of other forms of life."
    raw_input("Next...")
    print "Noone ever sent you a signal back. Yet."
    raw_input("Next...")
    #global mood
    #mood -= 1

# meow ()

def sleep():
    print "Your energy slowly fades and you feel that you need some rest."
    raw_input("Next...")
    print "You find a cozy corner on the sofa and curl up, covering your nose with the tip of your tail."
    raw_input("Next...")
    print "What was that song you liked?"
    raw_input("Next...")
    print "Aha, here it is: https://www.youtube.com/watch?v=n-3x1FZE-no"
    raw_input("Next...")
    print "Soft kitty, warm kitty, little ball of fur..."
    raw_input("Next...")
    print "Happy kitty, sleepy kitty, purr, purr, purr..."
    raw_input("Next...")
    #global mood
    #mood += 1

# sleep()

def watch_birds():
    print "It all started as an ordinary day."
    raw_input("Next...")
    print "But suddenly you hear nasty pigeons mocking at you from the outside."
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
        print "(ﾐⓛ.ⓛ ﾐ)✧"
        raw_input("Next...")
        print "Pigeons were not expecting that! They crap thier pants and run away ignominiously!"
        raw_input("Next...")
        #global mood
        #mood += 1
    elif choice in ("2", "ignore"):
        print "After a few seconds you realize that they're not worth it. Ignorance is the best weapon."
        raw_input("Next...")
    elif choice in ("3", "kill"):
        print "You gallop towards the balcony, ready to catch and defeat!"
        raw_input("Next...")
        print "But somewhere along the way you slip on the wet floor and miss the hit."
        raw_input("")
        finish("Pigeons gaggle at your clumsiness, you feel defeated.")
    else:
        print "What was that?! Start over."
        watch_birds()

# watch_birds()

def eat():
    print "You start feeling a bit hungry. Time to grab some food."
    raw_input("Next...")
    print "You go check your food bowl and it's empty!"
    raw_input("Next...")
    print "Your human seems to be sleeping on the couch."
    raw_input("Next...")
    print "How are you gonna wake her up?"
    raw_input("Next...")
    print "Available options:"
    print "1. Meow"
    print "2. Sleep"
    print "3. Purr"

    human_asleep = True
    meow_second_try = False
    sleep_second_try = False
    counter = 0
    hint = "Hint: persistance is the key!"

    while counter <= 4:

        print "Your move is: meow, sleep or purr?"
        choice = raw_input("---> ")

        if choice in ("1", "meow") and meow_second_try:
            counter += 1
            print counter
            meow()
            finish("Your human gets angry at you making loud meowy noises and throws a pillow at you!")
        elif choice in ("1", "meow") and not meow_second_try:
            counter += 1
            print counter
            meow()
            meow_second_try = True
            print "Can't she hear you starving or what?"
            raw_input("Next...")

        elif choice in ("2", "sleep") and not sleep_second_try:
            counter += 1
            print counter
            print "You decide to take a nap by your human's side."
            sleep_second_try = True
            raw_input("Next...")
            sleep ()

        elif choice in ("2", "sleep") and sleep_second_try:
            counter += 1
            print counter
            sleep ()
            print "You dream of juicy meatballs and fresh salmon steaks."
            raw_input("Next...")

        elif choice in ("3", "purr") and human_asleep:
            counter += 1
            print counter
            purr()
            human_asleep = False
            print "But your human seems to be still sleeping. What do you do?"
            raw_input("Next...")
            print hint
            raw_input("Next...")

        elif choice in ("3", "purr") and not human_asleep:
            counter += 1
            print counter
            purr()
            print "Well that strategy seems to work out. Your human wakes up and feeds you. Nice!"
            raw_input("Next...")
            #global mood
            #mood += 1
            play()
        else:
            finish("That didn't help. Game over.")

def play():
    print "You feel a boost of energy. Time to play!"
    print "What will you play this time?"
    print "1. Hide-and-seek"
    print "2. Chase your tail"
    print "3. Hunt your human"

    choice = raw_input("---> ")

    if choice in ("1", "hide", "seek"):
        print "You move the wardrobe door, jump on the upper shelf, lurk and watch your human calling your name along with 'Ksss-kss-kss!'"
        raw_input("Next...")
        print "Poor creature, no way she's gonna find you here."
        raw_input("Next...")
        print "You're a ninja-super-kitty! Time for your triumph!"
        print "(=♡ + ♡=)"
        raw_input("Next...")
        play ()

    elif choice in ("2", "chase", "tail"):
        print "What was that song you liked?"
        raw_input("Next...")
        print "Aha, here it is: https://www.youtube.com/watch?v=PGNiXGX2nLU"
        raw_input("Next...")
        print "'You spin me right round,"
        raw_input("Next...")
        print "baby, right round,"
        raw_input("Next...")
        print "like a record baby,"
        raw_input("Next...")
        print "right round round round!'"
        raw_input("Next...")
        print "Ooops! You start feeling a little vertigo. Maybe enough is enough."
        raw_input("Next...")

    elif choice in ("3", "hunt", "human"):
        print "What was that song you liked?"
        raw_input("Next...")
        print "Aha, here it is: https://www.youtube.com/watch?v=ZtUAxpEIsRc"
        raw_input("Next...")
        print "'Just because it's the middle of the night"
        raw_input("Next...")
        print "That don't mean I won't hunt you down"
        raw_input("Next...")
        print "Cause up, in, deep inside"
        raw_input("Next...")
        print "It's pullin' me and I want your love...'"
        raw_input("Next...")
        print "You hide behind the bathroom door and jump out unexpectedly when your human passes by."
        print "¯\_₍⸍⸌̣ʷ̣̫⸍̣⸌₎_/¯"
        raw_input("Next...")
        print "Aha! Gotcha! You bite her leg (with love) and run away."
        print "Mission complete. Congrats!"
        print "☆(=^ ◡ ^=)☆"

    else:
        finish("That didn't help. Game over.")


start()
watch_birds()
eat()
