# Character Input
# Exercise 1 from PracticePython.
#
# Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.
#
# Extras:
#
# Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
# Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)
#
#

name = input('What is your Name?')
age = int(input('How old are you?'))
year100 = (100 - age) + 2017
print('Howdy ' + name + '! You will turn 100 in ' + str(year100))

# Extra Section
repeats = int(input('How many repeats?'))
print(repeats * ('Howdy ' + name + '! You will turn 100 in ' + str(year100) + '\n'))
