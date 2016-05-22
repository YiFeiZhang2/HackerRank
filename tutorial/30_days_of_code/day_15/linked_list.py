#!/usr/local/bin/python3

class Node:
	def __init__(self,data):
		self.data = data
		self.next = None

class Solution:
	def display(self,head):
		current = head
		while current:
			print(current.data, end=' ')
			current = current.next

	def insert(self, head, data):
		if head is None:
			self.head = Node(data)
		else:
			new_Node = Node(data)
			current = self.head
			while current.next is not None:
				current = current.next
			current.next = new_Node
		return self.head

mylist = Solution()
T = int(input())
head = None
for i in range(T):
	data = int(input())
	head = mylist.insert(head,data)
mylist.display(head);
