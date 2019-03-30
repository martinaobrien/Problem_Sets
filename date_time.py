#Martina O'Brien 30 March 2019
#Problem Set 8 - datetime
# Program to output the current date and time using the strftime () method
# Reference https://www.w3schools.com/python/python_datetime.asp
import datetime 
#The datatime module is a method for formatting date object for python programs
x = datetime.datetime.now()
#brings in datetime for today or now

# The method is called strftime, and takes one parameter, format, to specify the format of the returned string.


# My variable x is being set up to bring in datetime for today or NOW.


# These if statements are finding out if the date has an st, nd, rd or th ending.

# If this if statement ends in a 1 it is true.
if x.strftime("%d") == "1" or x.strftime("%d") == "21" or x.strftime("%d") == "31":
    # As this statement was true it will print the Day of the Week, Month, Date, 'st', Year, 'at', Hour, ':',
    # Minute and (AM or PM).
    print(x.strftime("%A, %B %dst %Y at %-I:%M%p"))

# If this elif statement ends in a 2 it is true.
elif x.strftime("%d") == "2" or x.strftime("%d") == "22":
    # As this statement was true it will print the Day of the Week, Month, Date, 'nd', Year, 'at', Hour, ':',
    # Minute and (AM or PM).
    print(x.strftime("%A, %B %dnd %Y at %-I:%M%p"))

# If this elif statement ends in a 3 it is true.
elif x.strftime("%d") == "3" or x.strftime("%d") == "23":
    # As this statement was true it will print the Day of the Week, Month, Date, 'rd', Year, 'at', Hour, ':',
    # Minute and (AM or PM).
    print(x.strftime("%A, %B %drd %Y at %-I:%M%p"))

# If none of the other statement ends are true then this else statement will be executed.
else:
    # As this statement was true it will print the Day of the Week, Month, Date, 'th', Year, 'at', Hour, ':',
    # Minute and (AM or PM).
    print(x.strftime("%A, %B %dth %Y at %-I:%M%p"))
