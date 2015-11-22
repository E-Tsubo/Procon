# -*- Coding: utf-8 -*-

#競技プログラミング用
from decimal import *
import sys

#バブルソート(安定なソート)
def bubbleSort(a,n):
	sw = 0
	for i in range(0,n-1,+1):
		#右端から、隣同士の値を比較して、入れ替えを実施
		#1ループ終わるごとに、左端にソート済みの数値がおかれるので、探索範囲が狭まる
		for j in range(n-1,i,-1):
			if a[j-1] > a[j]:
				tmp = a[j-1]
				a[j-1] = a[j]
				a[j] = tmp
				sw += 1

	print(*a)
	return sw

def main():
	n = int(input())
	a = list(map(int, input().split(" ")))
	sw = bubbleSort(a,n)
	print(sw)

if __name__ == '__main__':
	main()
