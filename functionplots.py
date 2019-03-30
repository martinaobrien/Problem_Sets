# Martina O'Brien 30 March 2019
# Title: Problem Set 10 - plot functions 
# Programme that displays a plot of the functions x x^2 and 2^x in the range [0,4]and display them in a graph.

#import mglearn
import matplotlib.pyplot as plt

X, y = mglearn.datasets.make_wave(n_samples=40) 
plt.plot(X, y, 'o') 
plt.ylim(0, 4) 
plt.xlabel("Feature") 
plt.ylabel("Target")
plt.show()