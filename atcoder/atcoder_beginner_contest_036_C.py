# -*- Coding: utf-8 -*-
from decimal import *
import sys
import io
import re

def main():
	n = int(input())
	A = []
	B = []
	
	for i in range(0,n):
		A.append(int(input()))
		B.append(0)
		
	minB = 0	
	min = 1000000000
	case = -1
	for j in range(0,n):
	
	
		for i in range(0,n):
			if min > A[i] and A[i] > case:
				min = A[i]
	
		for i in range(0,n):
			if min == A[i]:
				B[i] = minB
				
		#Re init.
		minB = minB + 1
		case = min
		min = 1000000000
		
	for i in range(0,n):
		print(B[i])
	
if __name__ == '__main__':
	main()
