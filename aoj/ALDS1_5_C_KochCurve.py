# -*- Coding: utf-8 -*-
from  math import *

cos60 = cos(radians(60))
sin60 = sin(radians(60))

def KochCurve(n, p1, p2):
	if n == 0:
		return;
	
	s = [0.0, 0.0]
	u = [0.0, 0.0]
	t = [0.0, 0.0]
	
	s[0] = (2.0*p1[0] + 1.0*p2[0])/3.0
	s[1] = (2.0*p1[1] + 1.0*p2[1])/3.0
	t[0] = (1.0*p1[0] + 2.0*p2[0])/3.0
	t[1] = (1.0*p1[1] + 2.0*p2[1])/3.0
	u[0] = (t[0]-s[0])*cos60 - (t[1]-s[1])*sin60 + s[0]
	u[1] = (t[0]-s[0])*sin60 + (t[1]-s[1])*cos60 + s[1]
	
	KochCurve(n-1, p1, s)
	print( "{x:.8f} {y:.8f}".format(x=s[0], y=s[1]) )
	KochCurve(n-1, s, u)
	print( "{x:.8f} {y:.8f}".format(x=u[0], y=u[1]) )
	KochCurve(n-1, u, t)
	print( "{x:.8f} {y:.8f}".format(x=t[0], y=t[1]) )
	KochCurve(n-1, t, p2)
	
def main():

	start = [0.0,0.0]
	end   = [100.0,0.0]

	n = int(input())
	
	print( "{x:.8f} {y:.8f}".format(x=start[0], y=start[1]) )
	KochCurve(n, start, end)
	print( "{x:.8f} {y:.8f}".format(x=end[0], y=end[1]) )
	
if __name__ == '__main__':
	main()