# -*- Coding: utf-8 -*-
from  math import *

#無理やり作ったので汚い。。

class Node(object):
	"""A Node for BinaryTree"""
    
	"Constructor"
	def __init__(self, parent = -1, left = -1, right = -1):
		self.parent = parent
		self.parentIdx = -1
		self.left = left
		self.leftIdx = -1
		self.right = right
		self.rightIdx = -1
		self.data = None
		
	def getParent(self):
		return self.parent
	
	def getParentIdx(self):
		return self.parentIdx
		
	def getLeft(self):
		return self.left
	
	def getLeftIdx(self):
		return self.leftIdx
		
	def getRight(self):
		return self.right
	
	def getRightIdx(self):
		return self.rightIdx
		
	def getData(self):
		return self.data
	
	def setParent(self, parent):
		self.parent = parent
	
	def setParentIdx(self, idx):
		self.parentIdx = idx
		
	def setLeft(self, left):
		self.left = left
		
	def setLeftIdx(self, leftIdx):
		self.leftIdx = leftIdx
		
	def setRight(self, right):
		self.right = right
	
	def setRightIdx(self, rightIdx):
		self.rightIdx = rightIdx
		
	def setData(self, data):
		self.data = data
	
def searchParent(tree, n, parent):
	for i in range(n):
		if tree[i].getData() == parent:
			return i
	
	return -1

def calcSibling(tree, u):
	parentIdx = tree[u].getParentIdx()
	if parentIdx == -1:
		return -1
	
	if tree[parentIdx].getLeft() == tree[u].getData():
		return tree[parentIdx].getRight()
	if tree[parentIdx].getRight() == tree[u].getData():
		return tree[parentIdx].getLeft()

def calcDegree(node):
	cnt = 0
	if node.getLeft() != -1:
		cnt = cnt + 1
	if node.getRight() != -1:
		cnt = cnt + 1
	return cnt
		
def calcDepth(tree, u):
	depth = 0
	while tree[u].getParent() != -1:
		u = tree[u].getParentIdx()
		depth = depth + 1
	return depth
	
def calcHeight(tree, u):
	hr = hl = 0
	if tree[u].getRight() != -1:
		#print(u, tree[u].getRightIdx())
		hr = calcHeight(tree, tree[u].getRightIdx()) + 1
	if tree[u].getLeft() != -1:
		#print(u, tree[u].getLeftIdx())
		hl = calcHeight(tree, tree[u].getLeftIdx()) + 1
	
	return max(hr, hl)
	
def calcNodeType(node):
	if node.getParent() == -1:
		return "root"
	elif node.getLeft() == -1 and node.getRight() == -1:
		return "leaf"
	else:
		return "internal node"

def preOrder(tree, u ):
	if u == -1:
		return
		
	print("", end=" ")
	print( tree[u].getData(), end="" )
	preOrder( tree, tree[u].getLeftIdx() )
	preOrder( tree, tree[u].getRightIdx() )
	
def inOrder(tree, u):
	if u == -1:
		return

	inOrder( tree, tree[u].getLeftIdx() )
	print("", end=" ")
	print( tree[u].getData(), end="" )
	inOrder( tree, tree[u].getRightIdx() )
	
def postOrder(tree, u):
	if u == -1:
		return
	
	postOrder( tree, tree[u].getLeftIdx() )
	postOrder( tree, tree[u].getRightIdx() )
	print("", end=" ")
	print( tree[u].getData(), end="" )

def main():

	n = int(input())
	tree = []
	for i in range(n):
		tree.append( Node() )
		
	for i in range(n):
		tmp = list(map(int, input().split(" ")))

		tree[i].setData(tmp[0])	
		tree[i].setLeft(tmp[1])
		tree[i].setRight(tmp[2])

	for i in range(n):	
		tmp = tree[i].getData()
		for j in range(n):
			if tree[j].getLeft() == tmp:
				tree[i].setParent(tree[j].getData())
				tree[i].setParentIdx(j)
				break
			elif tree[j].getRight() == tmp:
				tree[i].setParent(tree[j].getData())
				tree[i].setParentIdx(j)
				break
		
		r = tree[i].getRight()
		l = tree[i].getLeft()
		for j in range(n):
			if tree[j].getData() == r:
				tree[i].setRightIdx(j)
				break;
		for j in range(n):
			if tree[j].getData() == l:
				tree[i].setLeftIdx(j)
				break
		
		
	#TreeWalk
	for i in range(n):
		if tree[i].getParent() == -1:
			start = i
			break

	print("Preorder");
	preOrder(tree, start)
	print("")
                        
	print("Inorder");
	inOrder(tree, start)
	print("")
	
	print("Postorder")
	postOrder(tree, start)
	print("")
	
	
if __name__ == '__main__':
	main()
