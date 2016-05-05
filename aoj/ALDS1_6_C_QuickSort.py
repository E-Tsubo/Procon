# -*- Coding: utf-8 -*-
from  math import *

# Partitionは、ある値を基準に小さいか大きいかで並び替えを行うアルゴリズム
# クイックソートは分割統治法に基づくが、この技術を分割の部分に利用している。
# クイックソートの入れ替えアルゴリズムはPartitionにより入れ替えを繰り返して、再統合しているに過ぎない。

def Partition(A, p, r):
	x = A[r][1]
	i = p - 1
	
	#jは0-番兵ひとつ前まで(j<rが条件)
	for j in range(p, r):
		if A[j][1] <= x:
			i = i + 1
			A[i], A[j] = A[j], A[i]
	
	#最後に基準としていた最後尾の数値を、A[i+1]に移動
	#Swap(A[i+1], A[r])　以下の記述がおすすめ
	A[i+1], A[r] = A[r], A[i+1]
	return (i+1)
	
def QuickSort(A, p, r):
	if( p < r):
		pos = Partition(A, p, r)
		QuickSort( A, p, pos-1)
		QuickSort( A, pos+1, r)
		
#安定性のチェックに、インポート時に付与した番号を利用している。
def CheckStable(A):
	for i in range(1,len(A)):
		if A[i-1][1] == A[i][1]:
			if A[i-1][2] > A[i][2]:
				return False
	return True

def main():

	n = int(input())
	A = []
	for i in range(n):
		mark, num = input().split(" ")
		A.append( [mark, int(num), i] )
		#i is check number for stable or unstable.
	
	QuickSort(A, 0, n-1)
	
	if CheckStable(A):
		print("Stable")
	else:
		print("Not stable")
	
	for i in A:
		print(i[0], i[1])
	
if __name__ == '__main__':
	main()