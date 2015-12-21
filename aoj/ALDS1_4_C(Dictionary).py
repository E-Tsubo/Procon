# -*- Coding: utf-8 -*-

#競技プログラミング用
from decimal import *
import sys

#Pythonにはsetがあるが、
#あえてハッシュ法のアルゴリズムを実装してみる
#衝突が発生した際の、回避方法にオープンアドレス法を利用
#再ハッシュの方法は、線形操作法


class HashTable(object):
    """A HashTable"""

    "Constructor"
    def __init__(self, func, size):
        self.size = 0
        self.hashSize = size
        self.hashFunc = func
        self.hashTable = [None]*size

    def _hashOpenAddress(h):
        #オープンアドレス法(線形探索)
        if (h+1) >= (self.hashSize-1):
            return 0
        else:
            return (h+1)

    def _hashFunc(self, key):
        return self.hashFunc(key, self.hashSize)

    def _searchKey(self, key):
        h = self.hashFunc(key, self.hashSize)
        cnt = 0
        while cnt < self.hashSize:
            tmp = self.hashTable[h]
            if tmp is None:
                break
            elif tmp == key:
                return h
            else:
                h = self._hashOpenAddress
                cnt += 1

        return -1

    def search(self, key):
        n = self._searchKey(key)
        if n >= 0:
            return self.hashTable[n]
        else:
            return None

    def insert(self, key, value):
        while True:
            h = self.hashFunc(key, self.hashSize)
            if self.hashTable[h] == None:
                self.hashTable[h] = value
                return True
            else:
                h = self._hashOpenAddress



hs = 1000000
#hs = n
def hf(key, hs):
    cnt = 1
    h = 0
    for i in range( (len(key)-1),-1,-1 ):
        if key[i] == 'A':
            h += cnt * 1
        elif key[i] == 'C':
            h += cnt * 2
        elif key[i] == 'G':
            h += cnt * 3
        elif key[i] == 'T':
            h += cnt * 4
        else:
            h += cnt * 5

        cnt *= 10

    return ( h % hs)

n = int(input())
ht = HashTable(hf, hs)

for i in range(n):
    inputs = input().split(" ")

    if inputs[0] == "insert":
        ht.insert(inputs[1], inputs[1])

    elif inputs[0] == "find":
        if ht.search(inputs[1]) == None:
            print("no")
        else:
            print("yes")
