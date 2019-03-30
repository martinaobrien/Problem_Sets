# Martina O'Brien - 25 - 03 - 2019
# Problem Set Programming and Scripting Code 6
# Output gives selected words in a string

sentence = (input("Enter your text here:")) # Input string needed for programme

str = sentence #users input is set as a string

every_second_word = str.split()[::2] 
# str.split() denotes what will happen to the string
#[::2] ensures that every second word is extracted and is outputted in a list 
#Reference:https://www.geeksforgeeks.org/python-string-split/
#Reference:https://www.pythonforbeginners.com/dictionary/python-split 

print (''.join(every_second_word))
# Using ''.join takes the quotation marks and commas away from the output, constructing a new sentence. 
# '' denotes was will be outputted between each of the words
# Reference: https://www.tutorialspoint.com/python3/string_join.htm

