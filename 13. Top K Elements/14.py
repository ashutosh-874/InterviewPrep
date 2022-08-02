# Frequency Stack (hard)#

# Design a class that simulates a Stack data structure, implementing the following two operations:

#     push(int num): Pushes the number ‘num’ on the stack.
#     pop(): Returns the most frequent number in the stack. If there is a tie, return the number which was pushed later.

# Example:

# After following push operations: push(1), push(2), push(3), push(2), push(1), push(2), push(5)

# 1. pop() should return 2, as it is the most frequent number
# 2. Next pop() should return 1
# 3. Next pop() should return 2

from heapq import heappop, heappush


class FrequencyStack:
    def __init__(self):
        self.max_heap = []
        self.count = 0

    def push(self, num):
        temp = []
        while self.max_heap:
            el = heappop(self.max_heap)
            if el[1] == num:
                heappush(self.max_heap, (el[0] - 1, num, self.count + 1))
                self.count += 1
                break
            else:
                temp.append(el)
        if not self.max_heap:
            heappush(self.max_heap, (-1, num, self.count + 1))
            self.count += 1
        for x in temp:
            heappush(self.max_heap, x)
            temp = []
        print(self.max_heap)

    def pop(self):
        if len(self.max_heap) == 0:
            return -1
        max_freq = self.max_heap[0][0]
        el = heappop(self.max_heap)
        temp = [el]
        while el[0] == max_freq:
            el = heappop(self.max_heap)
            temp.append(el)
        minCount = float('inf')
        res = None
        for item in temp[:-1]:
            if item[2] < minCount:
                res = item
                minCount = item[2]
            
            heappush(self.max_heap, item)


        


def main():
    frequencyStack = FrequencyStack()
    frequencyStack.push(1)
    frequencyStack.push(2)
    frequencyStack.push(3)
    frequencyStack.push(2)
    frequencyStack.push(1)
    frequencyStack.push(2)
    frequencyStack.push(5)
    # print(frequencyStack.pop())
    # print(frequencyStack.pop())
    # print(frequencyStack.pop())


main()







