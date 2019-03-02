# Martina O'Brien: 24 - 02 - 2019
# Problem Set Programming and Scripting Code 1
#Calculate the sum of all factorials of positive integer

# Input variable needed for calculation
# Int method returns an integer as per python programming
# input "Enter Number" will be visible on the user interface
# setting up variables to be used later in while loop

start = int (input ('Enter Number: '))
ans = 0
# ans = 0 and 0 is the value that the loop begins calculating
i = 1
# i = 1 as the starting point
while i <= start:
    ans = ans + i
    i = i + 1

# ans will continue to increase by the value of i as it progresses through the while loop
# i will increase by 1 each time it goes through while loop.
# This will continue until the value i reaches the start number

print(ans)
# Print is the funtion used to display the sum of all factorials of positive integer inputted
# As print is not contained through indentation in the previous, it displays one figure as ans