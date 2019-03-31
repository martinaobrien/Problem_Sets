#Martna O'Brien 10 - 03 - 2019
#Problem St 5 primes
#Calculation of whether or not a positive number is a prime number

number = int (input ('Enter Number: '))
if number > 0:
    if number > 1: 
        for i in range (2, number): # use of for loop to repeatedly execute some code statement
             if (number % i) == 0: # this argument will check if the range of numbers between 2 and that number, checking each potential factor
                print ('This is not a prime number')
                break # breaks out of the loop entirely
        else: # else statement is executed  if not of the factors divide the inputted number
            print(number,"is a prime number")
    else: #else statement is executed if integer is 1
        print ('This is not a prime number')
else: #else statement is executed if the inputted integer is not positive
        print ('This is not a positive integer')


    



       

