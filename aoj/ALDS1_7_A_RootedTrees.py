# -*- Coding: utf-8 -*-
from  math import *

class Node(object):
	"""A Node for RootedTree"""
    
	"Constructor"
	def __init__(self, parent = None, left = None, right = None):
		self.parent = parent
		self.leftchild = left
		self.rightsibiling = right
		
	def getParent(self):
		return self.parent
	
	def getLeftChild(self):
		return self.leftchild
		
	def getRightSibiling(self):
		return self.rightsibiling
		
	def setParent(self, parent):
		self.parent = parent
	
	def setLeftChild(self, left):
		self.leftchild = left
		
	def setRightSibiling(self, right):
		self.rightsibiling = right

def main():

	n = int(input())
	tree = []
	for i in range(n):
		tree.append( Node( None, None, None ) )
		
	for i in range(n):
		tmp = list(map(int, input().split(" ")))
		if tmp[1] > 0:
			tree[tmp[0]].setLeftChild(tmp[2])
		
		out = []
		for j in range(2,2+tmp[1]):
			#print(i,j)
			out.append(tmp[j])
			
			tree[tmp[j]].setParent( tmp[0] )
			if j < (tmp[1]+1):
				tree[tmp[j]].setRightSibiling(tmp[j+1])
			
		#print(i, tree[i].getParent(), out)
		
	#RootTreeの節を遡る。
	for i in range(n):
		print(i, tree[i].getParent(), end=" " )
		if( tree[i].getLeftChild() != None ):
			print( tree[i].getLeftChild(), end=" ")
			
			flag = True
			num = tree[i].getLeftChild()
			while( flag ):
				tmp = tree[num].getRightSibiling()
				if( tmp != None ):
					print( tmp, end=" ")
					num = tmp
				else:
					flag = False
		
		print()
	
if __name__ == '__main__':
	main()