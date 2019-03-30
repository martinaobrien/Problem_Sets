# Martina O'Brien - 25 - 03 - 2019
# Problem Set Programming and Scripting Code 6
# Output gives selected words in a string

# Input string needed for programme

sentence = (input("Enter your text here:"))

str = sentence

every_second_word = str.split()[::2]

print (every_second_word)

