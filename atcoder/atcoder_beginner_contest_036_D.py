# -*- Coding: utf-8 -*-
from decimal import *
import sys
import io
import re
import itertools

def main():

	l = range(1, 11) # [1, 2, 3, 4, 5]

	# lから要素を2つ選んで並べる
	# 重複は考慮しない
	# 順序は考慮する(順列
	cnt = 0
	for elem in itertools.permutations(l, 2):
		print(elem) # elemには並べた要素のタプルが代入される
		cnt = cnt + 1
		
	print(cnt)

if __name__ == '__main__':
	main()
