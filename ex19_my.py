# Creating my own function and run it 10 different ways
def dasha_weather_function(weather_condition, temperature):
    print "It looks like it's %s today!" % weather_condition
    print "And the temperature is %s degrees C" % temperature
    print "Today will be a good day!\n"

weather_condition = raw_input("What is the weather today? ")
temperature = raw_input("What is the temperature today? ")

dasha_weather_function(weather_condition, temperature)

dasha_weather_function("Windy", 3)

dasha_weather_function("pretty " + weather_condition, "about " + temperature)
