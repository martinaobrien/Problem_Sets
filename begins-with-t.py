# Martina O'Brien: 25 - 02 - 2019
# Problem Set Programming and Scripting Code 2
# Whether or not today's is a day that begins with the letter T

#Import function to output days of the week (reference: classnotes)

import datetime

# This if statement is an or argument that is validating the current day
# It checks whether the day is Tuesday (1) or Thursday (3)as they start with T
# or is an operator (reference:https://www.tutorialspoint.com/python3/python_basic_operators.htm)
if (datetime.datetime.today().weekday() == 1) or (datetime.datetime.today().weekday() == 3):
    print("Yes - today begins with T")
#This else statement prints out all other days
else: 
    print ("No - today does not begin with a T")