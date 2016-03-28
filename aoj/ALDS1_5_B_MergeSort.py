from decimal import *
from math import *
import sys

cnt = 0
	
def MergeSort(A, left, right):
	if left+1 < right:
		mid = floor( (left+right)/2 )
		MergeSort(A, left, mid)
		MergeSort(A, mid, right)
		#担当範囲(A[left-right])の並び替えが完了したので交換
		#当然だが再起処理なので、一番深いところから以下の関数が動く
		Merge(A, left, mid ,right)
		
	return
		
def Merge(A, left, mid, right):
	global cnt
	
	#時間超過となったので改修
	#繰り返しは時間かかるから、配列の扱い方で
	#n1 = mid - left
	#n2 = right - mid
	#L = [0]*(n1+1)
	#R = [0]*(n2+1)
	
	#for i in range(0,n1):
	#	L[i] = A[left+i]
	#for i in range(0,n2):
	#	R[i] = A[mid+i]
	#L[n1] = R[n2] = float("INF")
	
	L = A[left:mid] + [1e9 + 1]
	R = A[mid:right] + [1e9 + 1]
	
	i = j = 0
	for k in range(left,right):
		cnt += 1
		if L[i] <= R[j]:
			A[k] = L[i]
			i += 1
		else:
			A[k] = R[j]
			j += 1
			
	return

def main():
	n = int(input())
	A = list(map(int, input().split()))

	MergeSort(A, 0, n)
	print(*A)
	print(cnt)

if __name__ == '__main__':
	main()
