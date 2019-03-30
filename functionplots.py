# Martina O'Brien 30 March 2019
# Title: Problem Set 10 - plot functions 
# Programme that displays a plot of the functions x x^2 and 2^x in the range [0,4]and display them in a graph.

#import mglearn
import matplotlib.pyplot as plt
import numpy as np

 
lower = int(input('enter lower: '))
# This variables 'lower' is going to allow the user to set the lower part of the range.
upper = int(input('enter upper: '))
# This variables 'upper' is going to allow the user to set the upper part of the range.

x = np.arange(lower, upper)
#x creates the range for lower and upper values

plt.plot (x,x)  
plt.xlabel("number") 
plt.ylabel("number")
plt.show()

