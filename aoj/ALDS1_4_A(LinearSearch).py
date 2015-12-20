# -*- Coding: utf-8 -*-

#競技プログラミング用
from decimal import *
import sys

#これが最も素直な実装
#さらに計算コストを減らすには、番兵を用いた実装を行う。
#これにより、forループの条件、比較演算の2回の計算が必要になるところを
#番兵か否かの1回で済む
def main():
    n = int(input())
    s = input().split(" ")
    q = int(input())
    t = input().split(" ")

    cnt = 0;
    for i in range(q):
        for j in range(n):
            if s[j] == t[i]:
                cnt += 1
                break

    print(cnt)

if __name__ == '__main__':
	main()
