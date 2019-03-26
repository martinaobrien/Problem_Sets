# Martina O'Brien - 25 - 03 - 2019
# Problem Set Programming and Scripting Code 4
# Calculation on a positive integer with loop statements

# Input variable needed for calculation
# Int method returns an integer as per python programming
# input "Enter Number" will be visible on the user interface
# Input will then be calculated as per loop statements
# setting up variables to be used later in while loop

i = int (input ('Enter Number: '))

if i >= 0: # integer has to be greater than 0, the if statement investigates whether an argument is true
    if i %2== 0: # this determines whether or not the integer is even
        print (i//2) #determines if the number is even
    elif i %2== 1:
        print (i *3 + 1)




    else: 
        print ('False')


else: 
    print('This is not a positive number')