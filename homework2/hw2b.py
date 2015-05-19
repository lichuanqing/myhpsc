#homework2 part b:make a module containing a function to solve polynominal.

'''
make the hw2a.py script more genearl by turning it into a module.
Demonstration module for quadratic interpolation.
Update this docstring to describe your code.
Modified by: Tranchin Lee
'''
import numpy as np
from numpy.linalg import solve
import matplotlib.pyplot as plt

def quad_interp(xi,yi):
	'''
	 Quadratic interpolation.  Compute the coefficients of the polynomial
    interpolating the points (xi[i],yi[i]) for i = 0,1,2.
    Returns c, an array containing the coefficients of
      p(x) = c[0] + c[1]*x + c[2]*x**2.
      
	(function to solve polynominal p(x)=c0+c1x+c2x*x,coe vector c will be returned. xi is a array which presentes the x-coordinate of the three points.yi is the y-coordinate.)
	
	'''
	#chech the input and print error message if not valid input
	error_message="xi and yi should have type numpy.ndarray"
	assert (type(xi) is np.ndarray ) and (type(yi) is np.ndarray),error_message
	
	error_message="xi and yi should have length 3"
	assert (len(xi)==3 ) and (len(yi) ==3),error_message

	#Matrix coe. A, Vector coe.b
	A=np.vstack([np.ones(3),xi,xi**2]).T
	b=yi

	#Solve linear equation for vector c
	c=solve(A,b)
	#print "the polynominal coefficients are:"
	#print c
	return c
	
def test_quad1():
	'''
	Test code, no return value or exception if test runs properly.
	make a test to the function quad_interp
	'''
	
	xi=np.array([-1.,0,2])
	yi=np.array([1.,-1,7])
	c=quad_interp(xi,yi)
	c_true=np.array([-1,0,2.])
	print "c	 :",c
	print "c_true:",c_true
	assert np.allclose(c,c_true),"Incorrect resutls c= %s, Expected c= %s" %(c,c_true)
if __name__=="__main__":
	print"Runing test---"
	test_quad1()
	

