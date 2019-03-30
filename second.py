#Martina O'Brien 30 March 2019
#Problem Set 9- second
# Program designed to execute every second line of a text file


with open('moby-dick.txt', 'r') as text_file:
# this opens the text document from the command line
# Reference http://book.pythontips.com/en/latest/open_function.html
# 'r' imports the readline function
# Refernence:https://cmdlinetips.com/2011/08/three-ways-to-read-a-text-file-line-by-line-in-python/
    count = 0
    # The count is set at zero for the for loop
    for line in text_file:
    #the for loop goes through each line in the text file
    # The count is looking at the line and adding 1 every time it runs through the for loop.
        count+=1
        # If the count is even and has no remainders then the if statement is true.
        if count % 2 == 0:
            # If the if statement is true it will print the line.
            print(line)