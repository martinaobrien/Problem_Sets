# Martina O'Brien - 25 - 03 - 2019
# Problem Set Programming and Scripting Code 4
# Calculation on a positive integer with loop statements

# Input variable needed for calculation
# Int method returns an integer as per python programming
# input "Enter Number" will be visible on the user interface
# Input will then be calculated as per loop statements
# Setting up variables to be used later in while loop
# Reference for code: adapted from https://www.webucator.com/blog/2015/07/collatz-conjecture-in-python/

i = int(input ('Enter Number: '))

if i >= 0: # integer has to be greater than 0, the if statement investigates whether an argument is true
    
    print(i)
    def collatz(number): 
        if number % 2 == 0: # determines whether or not the integer is even
            print(number // 2) 
            return number // 2 # function returns the control to the function that callled it rather than ending the function

        elif number % 2 == 1: # i is odd and is calculated as per programming
            result = 3 * number + 1 
            print(result)
            return result #function returns the control to the function that callled it rather than ending the function


    while i != 1:
        i = collatz(int(i)) # collates the numbers output in the loop statement
else: 
    print('This is not a positive number')