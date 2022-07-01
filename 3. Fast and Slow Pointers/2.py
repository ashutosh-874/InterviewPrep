# Given the head of a LinkedList with a cycle, find the length of the cycle.

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def find_cycle_length(head):
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return calculate_cycle_length(slow, fast)
    return False


def calculate_cycle_length(slow, fast):
    cycle_length = 0
    fast = fast.next
    while True:
        cycle_length += 1
        if slow == fast:
            return cycle_length
        fast = fast.next

def main():
    head = Node(1)
    head.next = head
    print("LinkedList cycle length: " + str(find_cycle_length(head)))
# def main():
#     head = Node(1)
#     head.next = Node(2)
#     head.next.next = Node(3)
#     head.next.next.next = Node(4)
#     head.next.next.next.next = Node(5)
#     head.next.next.next.next.next = Node(6)
#     head.next.next.next.next.next.next = head.next.next
#     print("LinkedList cycle length: " + str(find_cycle_length(head)))

#     head.next.next.next.next.next.next = head.next.next.next
#     print("LinkedList cycle length: " + str(find_cycle_length(head)))


main()