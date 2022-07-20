
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end=" ")
            temp = temp.next
        print()


# def reverse_sub_list(head, p, q):
    
#     count, temp, lead = 1, None, head
#     start_rev, end_rev = None, None
    
#     while head is not None:

#         if count == p - 1:
#             start_rev = head
#         if count == p:
#             end_rev = head

#         if count >= p and count <= q:
#             next = head.next
#             head.next = temp
#             temp = head
#             head = next
#             if count == q:
#                 if start_rev: start_rev.next = temp
#                 else: lead = temp
#                 end_rev.next = head
#         else:
#             head = head.next
            
#         count += 1

    

#     return lead


def reverse_sub_list(head, p, q):

    dummy_node = Node(0, head)

    dummy, cur = Node(0, head), head

    # 1. reach node at position p
    for _ in range(p - 1):
        dummy, cur = cur, cur.next

    # 2. reverse from left to right
    prev = None
    for i in range(q - p + 1):
        tempNext = cur.next
        cur.next = prev
        prev, cur = cur, tempNext

    # 3. Update Pointers
    dummy.next.next = cur
    dummy.next = prev

    return dummy_node.next


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    result = reverse_sub_list(head, 2, 5)
    print("Nodes of reversed LinkedList are: ", end='')
    result.print_list()


main()
