#Martina O'Brien 10/3/2019
#Problem Set 7 - squareroots
#Programming Code to determining the squareroots of positive floating point numbers

## Reference for try and expect https://www.w3schools.com/python/python_try_except.asp

while True: # this loop will run to allow the user to input a value again if they do not enter a positive integer
    try:
        num = input("Please enter a positive number: ")  # Here the user will enter positive number.
        number = float(num) # using a float(num) to allow numbers with decimal points
    except ValueError:
        print('Sorry this is not a number. Can you please try again and enter a positive number.')
        # If the value is entered is correct then the value will move to the next statement.
        continue #continue to the next interation of the loop
    
    if number <= 0:
            print('Please enter a number greater than zero') 
            # to ensure that the user inputs a positive number

    break
    # break from the while loop to the next variable

number_sqrt = (number ** 0.5)
# Using ** 0.5 gives the squareroot of the num inputted
# Using %0.1f returns the answers to one decimal point

print("The square root of %0.1f is approx %0.1f" %(number, number_sqrt))
# print the result of the variable to one decimal place. 
