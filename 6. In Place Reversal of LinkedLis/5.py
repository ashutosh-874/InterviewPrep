# Rotate a LinkedList (medium)#

# Given the head of a Singly LinkedList and a number ‘k’, rotate the LinkedList to the right by ‘k’ nodes.


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


    def get_length(self):
        l = 0
        temp = self
        while temp is not None:
            l += 1
            temp = temp.next
        return l

def rotate(head, rotations):

    l = head.get_length()

    print(l)
    if rotations == 0 or l <= 1:
        return head

    if rotations < l:
        rotations = l - rotations + 1
    elif rotations % l == 0:
        print("I am here")
        return head
    else:
        rotations = l - rotations % l + 1

    cur = head
    
    s_s, s_e = head, None
    f_s, f_e = None, None

    count = 1
    while cur:
        if count == rotations - 1:
            s_e = cur
        elif count == rotations:
            f_s = cur
        if not cur.next:
            f_e = cur
        
        cur = cur.next
        count += 1

    f_e.next = s_s
    s_e.next = None

    return f_s






def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    # head.next.next.next.next.next = Node(6)

    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    result = rotate(head, 5)
    print("Nodes of rotated LinkedList are: ", end='')
    result.print_list()


main()
