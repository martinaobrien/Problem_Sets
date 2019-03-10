#Martina O'Brien 10/3/2019
#divisors
#Print all numbers between 1,000 and 10,000 that are divisble by 6 but not 12

#Input integer needed for calculation between the range of 1,000 and 10,000
#Firstly, need to be able to print range between 1,000 and 10,000. Lower level is set with code =int(input ('Enter Number in lower range:')) 
# Secondly, need to be able to print range between 1,000 and 10,000. Upper level is set with code = int (input ('Enter Number in upper range:'))
#Reference: 
# This is vital for setting the computational range on in for loop

lower = int (input ('Enter Number in lower range: '))
upper = int (input ('Enter Number in upper range: '))
for i in range (lower, upper):
    if (i%6==0):
        print (i)

