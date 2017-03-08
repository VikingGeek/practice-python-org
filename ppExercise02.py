# Odd or Even
# Exercise 2 from OracticePython.org
#
# Exercise 2 (and Solution)
#
# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?
#
# Extras:
#
# If the number is a multiple of 4, print out a different message.
# Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
#

myNum = int(input('Pick a number?'))
if myNum % 4 == 0:
	stype ='divisible by 4.'
elif myNum % 2 == 0:
	stype = ' even.'
else:
	stype = ' odd.'
print('Your number was ' + stype)

mynum = int(input('Pick a second number?'))
mycheck = int(input('Pick a smaller third number?'))
if mynum % mycheck == 0:
	notdiv =''
else:
	notdiv = 'not '
	
print(str(mynum) + ' is ' + notdiv + 'divisible by ' + str(mycheck))
