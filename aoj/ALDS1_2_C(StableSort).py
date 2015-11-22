# -*- Coding: utf-8 -*-

#競技プログラミング用
from decimal import *
import sys

#バブルソート(安定なソート)
def bubbleSort(a,n):
	for i in range(0,n-1,+1):
		for j in range(n-1,i,-1):
			#入力の先頭に文字が入るとのこと。
			#比較は、文字後方の数字とのことから、
			#比較部分のみ通常のソート関数を修正
			if a[j-1][1:] > a[j][1:]:
				tmp = a[j-1]
				a[j-1] = a[j]
				a[j] = tmp

	print(*a)

#選択ソート
def selectionSort(a,n):
	for i in range(0,n):
		minj = i
		for j in range(i+1,n):
			#入力の先頭に文字が入るとのこと。
			#比較は、文字後方の数字とのことから、
			#比較部分のみ通常のソート関数を修正
			if a[minj][1:] > a[j][1:]:
				minj = j

		if minj != i:
			a[minj],a[i] = a[i],a[minj]

	print(*a)


def main():
	n = int(input())
	a = input().split(" ")
	#aをそのまま両方の関数で利用しないように。参照渡しなので。
	b = a[:]

	bubbleSort(a,n)
	print("Stable")
	selectionSort(b,n)
	if a != b:
		print("Not stable")
	else:
		print("Stable")

if __name__ == '__main__':
	main()
