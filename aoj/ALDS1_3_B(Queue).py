# -*- Coding: utf-8 -*-

#競技プログラミング用
from decimal import *
import sys

# キューを利用したタスクスケジューラ
def scheduler(n,q,name,time):
	calctime = 0;

	while len(time) > 0:
		process_n = name.pop(0)
		process_t = time.pop(0)

		if (process_t-q) > 0:
			name.append(process_n)
			time.append(process_t-q)
			calctime += q
		else:
			print(process_n,end=" ")
			print(calctime+process_t)
			calctime += process_t

def main():
	# Input Step
	n,q = map(int, input().split(" "))
	queue_n = []
	queue_t = []
	for i in range(0,n):
		tmp = input().split(" ")
		queue_n.append(tmp[0])
		queue_t.append(int(tmp[1]))

	# Calc Step
	scheduler(n,q,queue_n,queue_t)

	# Output Step

if __name__ == '__main__':
	main()

# メモ
# Solutionで見つけたコードから一部拝借させていただいた。
# こういう書き方は簡潔でいいなと思い
#
# collectionというのがあるのね。
# from collections import deque
# n, q = (int(s) for s in input().split())
# que = deque()
# for i in range(n):
#     name, ts = input().split()
#
# 入れ子にして格納しておけば楽だね。
#     que.append((name, int(ts)))
#
#
#    name, time = que.popleft()
