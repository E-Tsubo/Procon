# -*- Coding: utf-8 -*-
from decimal import *
import sys

def main():
	a = list(map(int, input().split(" ")))
	cnt = 0;
	
	for i in range(0, 1000):
		if a[1] <= 0:
			break;
		a[1] = a[1] - a[0]
		cnt = cnt + 1
	
	print(cnt)

if __name__ == '__main__':
	main()
