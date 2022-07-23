# Design a class to calculate the median of a number stream. The class should have the following two methods:

#     insertNum(int num): stores the number in the class
#     findMedian(): returns the median of all numbers inserted in the class

# If the count of numbers inserted in the class is even, the median will be the average of the middle two numbers.

# Example 1:

# 1. insertNum(3)
# 2. insertNum(1)
# 3. findMedian() -> output: 2
# 4. insertNum(5)
# 5. findMedian() -> output: 3
# 6. insertNum(4)
from heapq import *

class MedianOfAStream:

    def __init__(self):
        self.small, self.large = [], []

    def insert_num(self, num):
        
        heappush(self.small, -num)

        if self.small and self.large and -(self.small[0]) > self.large[0]:
            heappush(self.large, -heappop(self.small))

        if len(self.small) - len(self.large) > 1:
            heappush(self.large, -heappop(self.small))
        
        if len(self.large) - len(self.small) > 1:
            heappush(self.small, -heappop(self.large))

        print(self.small, self.large)

    def find_median(self):

        if len(self.small) > len(self.large):
            return -self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        else:
            return (-self.small[0] + self.large[0]) / 2


def main():
    medianOfAStream = MedianOfAStream()
    medianOfAStream.insert_num(3)
    medianOfAStream.insert_num(1)
    print("The median is: " + str(medianOfAStream.find_median()))
    medianOfAStream.insert_num(5)
    print("The median is: " + str(medianOfAStream.find_median()))
    medianOfAStream.insert_num(4)
    print("The median is: " + str(medianOfAStream.find_median()))


main()
  