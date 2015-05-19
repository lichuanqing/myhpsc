''' homework2 Get some experience with Python and numpy
Get experience writing a Python function and unit test.
'''
"""
Demonstration script for quadratic interpolation.
Update this docstring to describe your code.
Modified by: Tranchin Lee
"""

import numpy as np
from numpy.linalg import solve
import matplotlib.pyplot as plt

# data points 
xi=np.array([-1.0,1.0,2.0])
yi=np.array([0,4.0,3.0])

#Matrix coe. A, Vector coe.b
A=np.vstack([np.ones(3),xi,xi**2]).T
b=yi

#Solve linear equation for vector c
c=solve(A,b)
print "the polynominal coefficients are:"
print c

#plot the curve p(x) and points 
x=np.linspace(-2,3,10001) #curve p(x) the x-corrdinate of points
y=c[0]+c[1]*x+c[2]*x*x

plt.figure(1) #open a figure file No1
plt.clf # clean the figure
plt.plot(x,y,'b-') #plot the curve with blue line
# Adding data points (the curve p(x) should go through the points)
plt.plot(xi,yi,'ro') #red circle
plt.ylim(-2,6)  #set y-axix range
plt.title("Data points and interpolating polynominal")
plt.savefig("hw2a.png") #save figure as hw2a.png
