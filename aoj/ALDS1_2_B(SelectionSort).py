# -*- Coding: utf-8 -*-

#競技プログラミング用
from decimal import *
import sys

#選択ソート
def selectionSort(a,n):
	sw = 0
	for i in range(0,n):
		minj = i
		#未ソートの部分に関して、最小の値の場所を見つける。
		#最小の値と、左端の値を入れ替える。
		#上記を繰り返して、ソート済みの範囲が増えて、探索範囲が狭まっていく
		for j in range(i+1,n):
			if a[minj] > a[j]:
				minj = j

		if minj != i:
			#tmp = a[minj]
			#a[minj] = a[i]
			#a[i] = tmp

			#Pythonでのワンライナースワップの書き方(初めて知った)
			a[minj],a[i] = a[i],a[minj]
			sw += 1

	print(*a)
	return sw

def main():
	n = int(input())
	a = list(map(int, input().split(" ")))
	sw = selectionSort(a,n)
	print(sw)

if __name__ == '__main__':
	main()
