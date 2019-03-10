#Martina O'Brien 10/3/2019
#Problem Set 7 - squareroots
#Programming Code to determining the squareroots of positive floating point numbers

import math # math function is imported
num = int(input ('Enter positive number: ')) #variable for the following code

if num >= 0: # integer has to be greater than 0, the if statement investigates whether an argument is trus
    print (format(math.sqrt(num), '.2f'))   # give 2 digits after the point
else:
    print ('This is not a positive number') # else statement will be executed if the if statement if proved to be false

