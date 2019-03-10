#Martna O'Brien 10 - 03 - 2019
#Problem St 5 primes
#Calculation of whether or not a positive number is a prime number

number = int (input ('Enter Number: '))
if number > 1:
    for i in range (2, number):
        if (number % i) == 0:
            print ('This is a prime number')
            break
else: 
    print ('This is not a prime number')

