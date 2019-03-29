# Martina O'Brien - 25 - 03 - 2019
# Problem Set Programming and Scripting Code 4
# Calculation on a positive integer with loop statements

# Input variable needed for calculation
# Int method returns an integer as per python programming
# input "Enter Number" will be visible on the user interface
# Input will then be calculated as per loop statements
# setting up variables to be used later in while loop

i = input ('Enter Number: ')

#if i >= 0: # integer has to be greater than 0, the if statement investigates whether an argument is true
    def collatz (number): #a python program to 
        if number %2== 0: # this determines whether or not the integer is even
            print (number//2) #determines if the number is even
            return number//2

        elif number %2== 1:
            result= (number *3 + 1)
             print (result)
             return result

    while i != 1:
        i = collatz(int(i))

#else: 
 #   print('This is not a positive number')