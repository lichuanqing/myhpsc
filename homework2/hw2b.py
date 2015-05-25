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

def cubic_interp(xi,yi):
	'''
	cubic ingterpolation.Compute the coefficients of the polynomial
    interpolating the points (xi[i],yi[i]) for i = 0,1,2,3.
    Returns c, an array containing the coefficients of
      p(x) = c[0] + c[1]*x + c[2]*x**2+c[3]*x**3.
      
	'''
		#chech the input and print error message if not valid input
	error_message="xi and yi should have type numpy.ndarray"
	assert (type(xi) is np.ndarray ) and (type(yi) is np.ndarray),error_message
	
	error_message="xi and yi should have length 4"
	assert (len(xi)==4 ) and (len(yi) ==4),error_message

	#Matrix coe. A, Vector coe.b
	A=np.vstack([np.ones(4),xi,xi**2,xi**3]).T
	b=yi
	print A
	print b
	#Solve linear equation for vector c
	c=solve(A,b)
	#print "the polynominal coefficients are:"
	#print c
	return c
	
def plot_cubic(xi,yi):
	'''
	call cubic_interp and plot the cure and interception points
	'''
	#call quad_interp to compute vector c
	c=cubic_interp(xi,yi)
	x=np.linspace(xi.min()-1,xi.max()+2,1000) #the range of x for curve
	y=c[0]+c[1]*x+c[2]*x*x+c[3]*x**3
	plt.figure(1)
	plt.clf()
	plt.plot(x,y,'b-') #blue line
	plt.plot(xi,yi,'ro')#red point
	plt.title("cubic polynominal and interpation")
	plt.savefig('cubic.png')

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

def test_cubic1():
	'''
	Test code, no return value or exception if test runs properly.
	make a test to the function cubic_interp
	'''
	
	xi=np.array([-1.,1.,2,3.])
	yi=np.array([-2.,0,7.,26.])
	c=cubic_interp(xi,yi)
	c_true=np.array([-1,0,0.,1.])
	print "c	 :",c
	print "c_true:",c_true
	assert np.allclose(c,c_true),"Incorrect resutls c= %s, Expected c= %s" %(c,c_true)
	
	
def plot_quad(xi,yi):
	'''
	take two points:xi,yi >call the function quad_interp > plot the curve and points.
	'''
	#call quad_interp to compute vector c
	c=quad_interp(xi,yi)
	x=np.linspace(xi.min()-1,xi.max()+2,1000) #the range of x for curve
	y=c[0]+c[1]*x+c[2]*x*x
	plt.figure(1)
	plt.clf()
	plt.plot(x,y,'b-') #blue line
	plt.plot(xi,yi,'ro')#red point
	plt.title("quadratic polynominal and interpation")
	plt.savefig('quadratic.png')
	return
if __name__=="__main__":
	print"Runing test---"
	test_quad1()
	

