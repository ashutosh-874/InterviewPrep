# Problem Statement#

# Given an array of ‘K’ sorted LinkedLists, merge them into one sorted list.

# Example 1:

# Input: L1=[2, 6, 8], L2=[3, 6, 7], L3=[1, 3, 4]
# Output: [1, 2, 3, 3, 4, 6, 6, 7, 8]

# Example 2:

# Input: L1=[5, 8, 9], L2=[1, 7]
# Output: [1, 5, 7, 8, 9]

from heapq import *


class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __lt__(self, other):
        return self.value <= other.value 


def merge_lists(lists):
    min_heap = []
    
    for l_list in lists:
        if l_list is not None:
            heappush(min_heap, l_list)
    
    
    
    el = heappop(min_heap)
    head = ListNode(el.value)
    current = head
    if el.next: heappush(min_heap, el.next)
    while min_heap:
        el = heappop(min_heap)
        current.next = ListNode(el.value)
        current = current.next
        if el.next: heappush(min_heap, el.next)
    
    return head


def main():
    l1 = ListNode(5)
    l1.next = ListNode(8)
    l1.next.next = ListNode(9)

    l2 = ListNode(1)
    l2.next = ListNode(7)
    # l2.next.next = ListNode(7)

    result = merge_lists([l1, l2])
    print("Here are the elements form the merged list: ", end='')
    while result != None:
        print(str(result.value) + " ", end='')
        result = result.next


main()

