#homework2 part b:make a module containing a function to solve polynominal.

'''
make the hw2a.py script more genearl by turning it into a module.
'''
def quad_interp(xi,yi):
	'''
	function to solve polynominal p(x)=c0+c1x+c2x*x,coe vector c will be returned. xi is a array which presentes the x-coordinate of the three points.yi is the y-coordinate.
	'''
	import numpy as np
	from numpy.linalg import solve
	#import matplotlib.pyplot as plt

	# data points 
	#xi=np.array([-1.0,1.0,2.0])
	#yi=np.array([0,4.0,3.0])

	#Matrix coe. A, Vector coe.b
	A=np.vstack([np.ones(3),xi,xi**2]).T
	b=yi

	#Solve linear equation for vector c
	c=solve(A,b)
	print "the polynominal coefficients are:"
	print c
	return c
	
def test_quad1():
	'''
	make a test to the function quad_interp
	'''
	from numpy import array
	
	xi=array([-1.,0,2])
	yi=array([1.,-1,7])
	c=quad_interp(xi,yi)
	
if __name__=="__main__":
	print"Runing test---"
	test_quad1()
	

