# -*- Coding: utf-8 -*-
from decimal import *
import sys
import io
import re

def main():
	n = int(input())
	S = []
	for i in range(0,n):
		S.append(input())
		
	
	for i in range(0,n):
		for j in range(n-1,0-1,-1):
			print(S[j][i], end="")
		print("")

if __name__ == '__main__':
	main()
