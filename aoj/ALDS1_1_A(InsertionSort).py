# -*- Coding: utf-8 -*-

#競技プログラミング用
from decimal import *
import sys

#挿入ソート
def insertionSort(a,n):
	print(*a)
	for i in range(1,n):
		tmp = a[i]
		j = i - 1
		#iより左側の部分で、a[i]より大きい値があれば、一つ上の数値と交換を繰り返す
		#a[i]より大きい値がなくなった段階で、a[i]を挿入して1ループの挿入が完了
		while j >= 0 and a[j] > tmp:
			a[j+1] = a[j]
			j = j - 1
		a[j+1] = tmp

		print(*a)

	return a

def main():
	n = int(input())
	a = list(map(int, input().split(" ")))
	b = insertionSort(a,n)

if __name__ == '__main__':
	main()
