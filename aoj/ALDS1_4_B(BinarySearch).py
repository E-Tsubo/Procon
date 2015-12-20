# -*- Coding: utf-8 -*-

#競技プログラミング用
from decimal import *
import sys
import math

#2分探索
def binarySearch(s,n,key):
    left = 0
    right = n-1
    while left <= right:
        mid = (left+right)//2
        if int(s[mid]) == key: #型に気を付けよう。。。
            return True
        elif int(s[mid]) > key:
            right = mid - 1
        else:
            left = mid + 1

    return False

def main():
    n = int(input())
    s = input().split(" ")
    q = int(input())
    t = input().split(" ")

    cnt = 0;
    for i in range(q):
        if  binarySearch(s,n,int(t[i])) == True :
            cnt += 1

    print(cnt)

if __name__ == '__main__':
	main()
