# -*- Coding: utf-8 -*-
import sys

def solve(n, A, i, m):
    if m == 0:
        return 1
    if i >= n:
        return 0

    result = solve(n, A, i+1, m) | solve(n, A, i+1, m-A[i])
    return result


n = int(input())
A = list(map(int, input().split(" ")))
q = int(input())
M = list(map(int, input().split(" ")))

for i in range(0,q):
	if solve(n, A, 0, M[i]) == True:
		print('yes')
	else:
		print('no')
