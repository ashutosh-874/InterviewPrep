# Reverse alternating K-element Sub-list (medium)#

# Given the head of a LinkedList and a number ‘k’, reverse every alternating ‘k’ sized sub-list starting from the head.

# If, in the end, you are left with a sub-list with less than ‘k’ elements, reverse it too.


from __future__ import print_function


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


def reverse_alternate_k_elements(head, k):
    
    dummy = Node(0, head)

    group_prev, group_start, cur = dummy, head, head

    cond = True

    while cur:
        
        if cond:
            prev = None
            for _ in range(k):
                if not cur:
                    # if wanna reverse the remaining nodes
                    break

                    # if dont wanna reverse the remaining nodes
                    # temp = None
                    # while prev:
                    #     nxt = prev.next
                    #     prev.next = temp
                    #     temp, prev = prev, nxt
                    # prev = temp
                    # break

                next = cur.next
                cur.next = prev
                prev, cur = cur, next

            group_prev.next = prev
            group_prev = group_start
            group_start = cur

        cond = not cond

        if not cond:
            group_prev.next = group_start
            for _ in range(k):
                if not group_start: break
                group_prev, group_start = group_start, group_start.next
                cur = group_start


    return dummy.next


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    head.next.next.next.next.next.next = Node(7)
    head.next.next.next.next.next.next.next = Node(8)

    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    result = reverse_alternate_k_elements(head, 2)
    print("Nodes of reversed LinkedList are: ", end='')
    result.print_list()


main()
