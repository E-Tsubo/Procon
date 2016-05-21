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
		
		#Too slow...
		#-------------------------------
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
		#-------------------------------
		
	"Constructor"
	def __init__(self):
		self.root = None

	def getRoot(self):
		return self.root
		
	def insert(self, data):
		tmp_node = self.Node(data)
		guess_parent = None
		x = self.root
		while x is not None:
			guess_parent = x
			if data < x.data:
				x = x.left
			else:
				x = x.right
				
		#tmp_node.setParent(guess_parent)
		tmp_node.parent = guess_parent
		if guess_parent is None: #If Tree is empty,
			self.root = tmp_node
		elif tmp_node.data < guess_parent.data:
			#guess_parent.setLeft(tmp_node)
			guess_parent.left = tmp_node
		else:
			#guess_parent.setRight(tmp_node)
			guess_parent.right = tmp_node
	
	def showPreorder(self, n):
		if n is None:
			return 
		
		print("", end= " ")
		print(n.data, end="")
		self.showPreorder(n.left)
		self.showPreorder(n.right)
		
	def showInorder(self, n):
		if n is None:
			return 
		
		self.showInorder(n.left)
		print("", end= " ")
		print(n.data, end="")
		self.showInorder(n.right)
		
	def find(self, key):
		x = self.root
		while( x is not None):
			if x.data == key:
				print("yes")
				return
			elif key < x.data:
				x = x.left
			else:
				x = x.right
		
		print("no")


tree = BinaryTree()
n = int(input())

for i in range(n):
	inputs = input().split(" ")
	
	if inputs[0] == "insert":
		tree.insert(int(inputs[1]))
	elif inputs[0] == "find":
		tree.find(int(inputs[1]))
	elif inputs[0] == "print":
		tree.showInorder(tree.getRoot())
		print("")
		tree.showPreorder(tree.getRoot())
		print("")
		
