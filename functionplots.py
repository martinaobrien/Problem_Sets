# Martina O'Brien 30 March 2019
# Title: Problem Set 10 - plot functions
# Programme that displays a plot of the functions x x^2 and 2^x in the range [0,4]and display them in a graph.

# import mglearn
import matplotlib.pyplot as plt
import numpy as np

lower = int(input('enter lower: '))
# This variables 'lower' is going to allow the user to set the lower part of the range.
upper = int(input('enter upper: '))
# This variables 'upper' is going to allow the user to set the upper part of the range.

x = np.arange(lower, upper)
# x creates the range for lower and upper values

plt.plot(x, x)
# Line displays x

plt.plot(x, x ** 2)
# Line 2 displays x^2

plt.plot(x, 2 ** x)
# Line 3 displays 2^x

# Graph labelling
My_title = f'Functions x, x^2 and 2^x in the range [{lower},{upper}]'
# Title is set us as a readable string.
plt.title(My_title, fontweight="bold")

plt.xlabel('x - axis')
# X axis is labelled

plt.ylabel('y - axis')
# X axis is labelled .
# Reference: https://matplotlib.org/api/text_api.html?highlight%3Dfontweight%23matplotlib.text.Text.get_fontweight&sa=D&source=hangouts&ust=1554075189421000&usg=AFQjCNE6Vi9Ok5-WxvK6qx136IKE2Y3wrQ


# Allocating labels for x and y axis
plt.xlabel("number")
plt.ylabel("number")
plt.show()