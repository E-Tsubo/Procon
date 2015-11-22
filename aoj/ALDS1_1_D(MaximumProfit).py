# -*- Coding: utf-8 -*-

#競技プログラミング用
import sys

def main():

	a,b,c,d = map( int, input().split(" ") )
	#at Python 3, raw_input is renamed to input
	#https://docs.python.org/3/whatsnew/3.0.html

	if b*c > a*d:
		print("TAKAHASHI")
	elif b*c < a*d:
		print("AOKI")
	else:
		print("DRAW")

if __name__ == '__main__':
	main()
