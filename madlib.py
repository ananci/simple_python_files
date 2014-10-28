############################################################
## MADLIB PROGRAM                                         ##
# This program will:
#   -Find out a user's name
#   -Greet the user
#   -Ask the user some questions
#   -Use their answers to make a madlib


#############################
##       GREET USER        ##

# Ask for their name
inp_user = raw_input("What is your name? ")
# Greet them
print "Hello {user}!".format(user = inp_user)

#############################
##      USER'S MADLIB      ##

# Let's tell the user what we are going to do
print "Enter the following to make a madlib:\n"

# This will let the user enter in the information we 
# need to make a madlib
inp_name = raw_input('Enter a name: ')
inp_color1 = raw_input('Enter a color: ')
inp_color2 = raw_input('Enter another color: ')
inp_body_part = raw_input('Enter a body part: ')
inp_noun1 = raw_input('Enter a noun: ')
inp_noun2 = raw_input('Enter another noun: ')
inp_noun3 = raw_input('Enter one more noun: ')
inp_verb1 = raw_input('Enter a verb: ')
inp_number1 = raw_input('Enter a number: ')
inp_number2 = raw_input('Enter another number: ')
inp_country1 = raw_input('Enter a country: ')
inp_country2 = raw_input('Enter another country: ')
inp_food = raw_input('Enter a food: ')
inp_song = raw_input('Enter a song: ')
inp_adjective = raw_input('Enter an adjective: ')

# This is the text for the madlib
mad_lib1 = "The {name} is an animal that has {color1} fur with {color2} spots on its {body_part}. Its tail is shaped like a(n) {noun1} which it uses to {verb1} {noun2}. An adult {name} may weigh more than {number1} pounds and stand over {number2} feet high. The {name} can be found only in {country1} and {country2}. Although its favorite food is {food} it also likes to eat {noun3}. If you ever see a(n) {name}, be sure not to ever sing \"{song}\". That song makes it {adjective}. Instead, give it a few {food} and be on your way."
### the words inside '{}' will be used to put our user's words into the mad lib

# It's almost done! Let's tell the user we are making a madlib
print "\n"
### \n prints an empty line
print "{user}'S MADLIB".format(user = inp_user.upper()) 
### inp_user.upper() will make the string in inp_user upper case
print "================================================="

# This takes the mad lib before and puts in all the information 
print mad_lib1.format(
    name = inp_name,
    color1 = inp_color1,
    color2 = inp_color2,
    body_part = inp_body_part,
    noun1 = inp_noun1,
    noun2 = inp_noun2,
    noun3 = inp_noun3,
    verb1 = inp_verb1,
    number1 = inp_number1,
    number2 = inp_number2,
    country1 = inp_country1,
    country2 = inp_country2,
    food = inp_food,
    song = inp_song,
    adjective = inp_adjective)