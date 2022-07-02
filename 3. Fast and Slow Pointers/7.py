# Rearrange a LinkedList (medium)#

# Given the head of a Singly LinkedList, write a method to modify the LinkedList such that the nodes from the second half of the LinkedList are inserted alternately to the nodes from the first half in reverse order. So if the LinkedList has nodes 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> null, your method should return 1 -> 6 -> 2 -> 5 -> 3 -> 4 -> null.

# Your algorithm should not use any extra space and the input LinkedList should be modified in-place.

# Example 1:

# Input: 2 -> 4 -> 6 -> 8 -> 10 -> 12 -> null
# Output: 2 -> 12 -> 4 -> 10 -> 6 -> 8 -> null 

# Example 2:

# Input: 2 -> 4 -> 6 -> 8 -> 10 -> null
# Output: 2 -> 10 -> 4 -> 8 -> 6 -> null

from __future__ import print_function


class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

	def print_list(self):
		temp = self
		while temp is not None:
			print(str(temp.value) + " ", end='')
			temp = temp.next
		print()


def reorder(head):
	# find mid of the linked list (if n is even mid here will give (mid - 1)th position )
	mid, fast = head, head.next
	while fast and fast.next:
		mid = mid.next
		fast = fast.next.next
	
	# reverse the second half
	prev, current = None, mid.next
	mid.next = None
	while current:
		nxt = current.next
		current.next = prev
		prev = current
		current = nxt

	# head.print_list()
	# prev.print_list()

	# merge the two halves
	p1, p2 = head, prev
	while p2:
		temp1 = p1.next
		temp2 = p2.next
		p1.next = p2
		p2.next = temp1
		p1 = temp1
		p2 = temp2


def main():
	head = Node(2)
	head.next = Node(4)
	head.next.next = Node(6)
	head.next.next.next = Node(8)
	head.next.next.next.next = Node(10)
	head.next.next.next.next.next = Node(12)
	# head.next.next.next.next.next.next = Node(13)
	reorder(head)
	head.print_list()


main()
