# Palindrome LinkedList (medium)#

# Given the head of a Singly LinkedList, write a method to check if the LinkedList is a palindrome or not.

# Your algorithm should use constant space and the input LinkedList should be in the original form once the algorithm is finished. The algorithm should have O(N)O(N)O(N) time complexity where ‘N’ is the number of nodes in the LinkedList.

# Example 1:

# Input: 2 -> 4 -> 6 -> 4 -> 2 -> null
# Output: true

# Example 2:

# Input: 2 -> 4 -> 6 -> 4 -> 2 -> 2 -> null
# Output: false

class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

	def print_list(self):
		temp = self
		while temp is not None:
			print(temp.value, end=' -> ')
			temp = temp.next
		print('null')


def findMiddleOfLinkedList(head):
	slow, fast = head, head
	while fast and fast.next:
		slow = slow.next
		fast = fast.next.next
	return slow

def reverse_linked_list(head):
	prev, current = None, head
	while current:
		temp = current.next
		current.next = prev
		prev = current
		current = temp
	return prev

def is_palindromic_linked_list(head):

	start, end = head, reverse_linked_list(findMiddleOfLinkedList(head))
	while end:
		if start.value != end.value:
			break
		start = start.next
		end = end.next
	return True


# 	# find mid of linked list (slow)
# 	slow, fast = head, head
# 	while fast and fast.next:
# 		slow = slow.next
# 		fast = fast.next.next

# 	# reverse_linked_list the second middle part 
# 	prev = None
# 	while slow:
# 		temp = slow.next
# 		slow.next = prev
# 		prev = slow
# 		slow = temp

# 	start, end = head, prev
# 	while end:
# 		if start.value != end.value:
# 			return False
# 		start = start.next
# 		end = end.next
# 	return True

def main():
	head = Node(2)
	head.next = Node(4)
	head.next.next = Node(6)
	head.next.next.next = Node(4)
	head.next.next.next.next = Node(3)

	print("Is palindrome: " + str(is_palindromic_linked_list(head)))

	# head.next.next.next.next.next = Node(2)
	# print("Is palindrome: " + str(is_palindromic_linked_list(head)))


main()
