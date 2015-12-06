class DoubleList(object):
    """A Doubly Linked List"""

    class Node(object):
        """A Node for Doubly Linked List"""

        "Constructor"
        def __init__(self, data, prev = None, next = None):
            self.data = data
            self.prev = prev
            self.next = next

    "Constructor"
    def __init__(self):
        self.nil = DoubleList.Node(None, None, None)
        self.nil.prev = self.nil
        self.nil.next = self.nil

    #先頭に追加
    def insert(self, data):
        tmp_node = DoubleList.Node(data, self.nil, self.nil.next)

        #入れ替えの順番に注意
        self.nil.next.prev = tmp_node #後続項目の差し替え
        self.nil.next = tmp_node      #先頭行の差し替え

    def search(self, key):
        s = self.nil.next
        while( s != self.nil ) and ( s.data != key ):
            s = s.next
        return s

    def deleteNode(self, node):
        if node == self.nil:
            return None
        node.prev.next = node.next
        node.next.prev = node.prev
        
    def deleteFirst(self):
        self.deleteNode(self.nil.next)

    def deleteLast(self):
        self.deleteNode(self.nil.prev)

    def deleteKey(self, key):
        node = self.search(key)
        self.deleteNode(node)

    def showData(self):
        s = self.nil.next
        data = []
        while s != self.nil:
            data.append(s.data)
            s = s.next

        print(" ".join(data))

import sys

dlist = DoubleList()
n = int(input())

for i in range(n):
    inputs = input().split(" ")

    if inputs[0] == "insert":
        dlist.insert(inputs[1])
    elif inputs[0] == "delete":
        dlist.deleteKey(inputs[1])
    elif inputs[0] == "deleteFirst":
        dlist.deleteFirst()
    elif inputs[0] == "deleteLast":
        dlist.deleteLast()

dlist.showData()
