# -*-coding: utf-8 -*-
name = 'Дашуля'
age = 27 # not a lie
height = 72 # inches
height_cm = round (height * 2.54)
weight = 167 # lbs
weight_kg = round(weight * 0.453592)
eyes = 'grey'
teeth = 'white'
hair = 'blond'

print "Let's talk about %s" % name
print "She is %s cm tall" % height_cm
print "She is %s kg heavy" % weight_kg
print "Actually that's not too heavy."
print "She's got %s eyes and %r hair." % (eyes, hair)
print "Her teeth are usually %s depending on the coffee." % teeth

print "If I add %d, %d and %d I get %d." % (age, height_cm, weight_kg, age + height_cm + weight_kg)
