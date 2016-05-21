# -*- Coding: utf-8 -*-
import sys
from  math import *

# Binary Search Implementation

"""A Binary Tree"""
class BinaryTree(object):

	"""A Node for Tree"""
	class Node(object):
		"Constructor"
		def __init__(self, data, parent = None, left = None, right = None):
			self.data = data
			self.parent = parent
			self.left = left
			self.right = right
		
		def getData(self):
			return self.data
			
		def setParent(self, parent):
			self.parent = parent
			
		def getParent(self):
			return self.parent
			
		def setLeft(self, left):
			self.left = left
			
		def getLeft(self):
			return self.left
		
		def setRight(self, right):
			self.right = right
	
		def getRight(self):
			return self.right
	
	"Constructor"
	def __init__(self):
		self.root = None

	def getRoot(self):
		return self.root
		
	def insert(self, data):
		tmp_node = self.Node(data)
		guess_parent = None
		x = self.root
		while x != None:
			guess_parent = x
			if data < x.getData():
				x = x.getLeft()
			else:
				x = x.getRight()
				
		tmp_node.setParent(guess_parent)
		if guess_parent == None: #If Tree is empty,
			self.root = tmp_node
		elif tmp_node.getData() < guess_parent.getData():
			guess_parent.setLeft(tmp_node)
		else:
			guess_parent.setRight(tmp_node)
	
	def showPreorder(self, n):
		if n == None:
			return 
		
		print("", end= " ")
		print(n.getData(), end="")
		self.showPreorder(n.getLeft())
		self.showPreorder(n.getRight())
		
	def showInorder(self, n):
		if n == None:
			return 
		
		self.showInorder(n.getLeft())
		print("", end= " ")
		print(n.getData(), end="")
		self.showInorder(n.getRight())		


tree = BinaryTree()
n = int(input())

for i in range(n):
	inputs = input().split(" ")
	
	if inputs[0] == "insert":
		tree.insert(int(inputs[1]))
	elif inputs[0] == "print":
		tree.showInorder(tree.getRoot())
		print("")
		tree.showPreorder(tree.getRoot())
		print("")
		
