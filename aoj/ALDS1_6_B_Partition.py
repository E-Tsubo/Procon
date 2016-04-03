# -*- Coding: utf-8 -*-
from  math import *

# Partitionは、ある値を基準に小さいか大きいかで並び替えを行うアルゴリズム
# クイックソートは分割統治法に基づくが、この技術を分割の部分に利用している。

def Partition(A, p, r):
	x = A[r]
	i = p - 1
	
	#jは0-番兵ひとつ前まで(j<rが条件)
	for j in range(p, r):
		if A[j] <= x:
			i = i + 1
			A[i], A[j] = A[j], A[i]
	
	#最後に基準としていた最後尾の数値を、A[i+1]に移動
	#Swap(A[i+1], A[r])　以下の記述がおすすめ
	A[i+1], A[r] = A[r], A[i+1]
	return (i+1)

def main():

	n = int(input())
	A = list(map(int, input().split(" ")))
	
	pos = Partition(A, 0, n-1)
	
	A = list(map(str, A))
	A[pos] = "[{}]".format(A[pos])
	print( " ".join(A) )
	
if __name__ == '__main__':
	main()