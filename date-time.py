#Martina O'Brien 30 March 2019
#Problem Set 8 - datetime
# Program to output the current date and time using the strftime () method
# Reference https://www.w3schools.com/python/python_datetime.asp

from datetime import datetime as dt 
#import the class datetime and module datetime to include in the program

def suffix(d): 
    return 'th' if 11<=d<=13 else {1:'st',2:'nd',3:'rd'}.get(d%10, 'th')
    # this returns the output based on certain conditions
    # .get is a function that is enabled if the other conditions are false instead of a error message
def custom_strftime(format, t): 
    #strftime converts date times to string formats. 
    #Reference: https://stackabuse.com/how-to-format-dates-in-python/
    return t.strftime(format).replace('{S}', str(t.day) + suffix(t.day))
    #returns string of day and its assigned suffix

x = custom_strftime('%A, %B {S} %Y at  %I:%M%p', dt.now())
    # x is being set up to bring all strftime values into a readable string 

print (x)
    # print wil display:day of week, month, date, suffix, year and time of execution.