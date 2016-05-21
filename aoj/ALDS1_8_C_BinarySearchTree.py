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
				#print("yes")
				return x
			elif key < x.data:
				x = x.left
			else:
				x = x.right
		
		#print("no")
		return None
		
	def delete(self, key):
		key_node = self.find(key)
		#print("-->test")
		#print(key_node.data)
		
		if key_node.left is not None and key_node.right is not None:
			next_node = self.getNext(key_node.right)
		
			#自身の右子以外
			if key_node.right != next_node:
			
				#移動させる右木最小節の右子の親を変更
				if next_node.right is None:
					next_node.parent.left = None
				else:
					next_node.parent.left = next_node.right
					next_node.right.parent = next_node.parent
	
				#削除節の子を右木最小節に連結
				key_node.right.parent = next_node
				next_node.right = key_node.right
				key_node.left.parent = next_node
				next_node.left = key_node.left
			
				#削除節の親情報を右木最小節に連結
				next_node.parent = key_node.parent
				
				#削除節の親節に対して、子情報を更新
				if key_node.parent.data < key_node.data:
					key_node.parent.right = next_node
				else:
					key_node.parent.left = next_node
			
			#自身の右子
			else:
				#削除節の子を右木最小節に連結
				# next_node = key_node.right
				next_node.parent = key_node.parent
				next_node.left = key_node.left
				
				#削除節の親情報を右木最小節に連結
				next_node.parent = key_node.parent

				#削除節の親節に対して、子情報を更新
				if key_node.parent.data < key_node.data:
					key_node.parent.right = next_node
				else:
					key_node.parent.left = next_node
			
		elif key_node.left is None and key_node.right is None:
			if key_node.left is None:
				key_parent = key_node.parent
				if key_node.data < key_parent.data:
					key_parent.left = None
				else:
					key_parent.right = None
			else:
				key_parent = key_node.parent
				if key_node.data < key_parent.data:
					key_parent.left = None
				else:
					key_parent.right = None
			
		else:
			if key_node.left is None:
				key_parent = key_node.parent
				key_node.right.parent = key_parent
				if key_node.data < key_parent.data:
					key_parent.left = key_node.right
				else:
					key_parent.right = key_node.right
			else:
				key_parent = key_node.parent
				key_node.left.parent = key_parent
				if key_node.data < key_parent.data:
					key_parent.left = key_node.left
				else:
					key_parent.right = key_node.left
		
	def getNext(self, key):
		tmp = key
		while(True):
			if tmp.left is None:
				return tmp
			else:
				tmp = tmp.left
					
tree = BinaryTree()
n = int(input())

for i in range(n):
	inputs = input().split(" ")
	
	if inputs[0] == "insert":
		tree.insert(int(inputs[1]))
	elif inputs[0] == "find":
		if tree.find(int(inputs[1])) is not None:
			print("yes")
		else:
			print("no")
	elif inputs[0] == "delete":
		tree.delete(int(inputs[1]))
	elif inputs[0] == "print":
		tree.showInorder(tree.getRoot())
		print("")
		tree.showPreorder(tree.getRoot())
		print("")
		
