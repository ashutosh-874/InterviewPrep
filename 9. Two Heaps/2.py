# Given an array of numbers and a number ‘k’, find the median of all the ‘k’ sized sub-arrays (or windows) of the array.

# Example 1:

# Input: nums=[1, 2, -1, 3, 5], k = 2
# Output: [1.5, 0.5, 1.0, 4.0]
# Explanation: Lets consider all windows of size ‘2’:

#     [ 1, 2, -1, 3, 5] -> median is 1.5
#     [1, 2, -1, 3, 5] -> median is 0.5
#     [1, 2, -1, 3, 5] -> median is 1.0
#     [1, 2, -1, 3, 5] -> median is 4.0

# Example 2:
 
# Input: nums=[1, 2, -1, 3, 5], k = 3
# Output: [1.0, 2.0, 3.0]
# Explanation: Lets consider all windows of size ‘3’:

#     [1, 2, -1, 3, 5] -> median is 1.0
#     [1, 2, -1, 3, 5] -> median is 2.0
#     [1, 2, -1, 3, 5] -> median is 3.0

from heapq import *
import heapq

class SlidingWindowMedian:

    def __init__(self):
        self.small, self.large = [], []
        self.result = []

    def find_median(self):
        if len(self.small) > len(self.large):
            return -self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        else:
            return (-self.small[0] + self.large[0]) / 2

    def remove_element(self, heap, element):
        ind = heap.index(element)
        heap[ind] = heap[-1]
        del heap[-1]
        if ind < len(heap):
            heapq._siftup(heap, ind)
            heapq._siftdown(heap, 0, ind)

    def find_sliding_window_median(self, nums, k):

        for idx, i in enumerate(nums):
            heappush(self.small, -i)

            if self.small and self.large and -self.small[0] > self.large[0]:
                heappush(self.large, -heappop(self.small))
            
            if len(self.small) - len(self.large) > 1:
                heappush(self.large, -heappop(self.small))

            if len(self.large) - len(self.small) > 1:
                heappush(self.small, -heappop(self.large))

            print(self.small, self.large)
            if len(self.small) + len(self.large) == k:
                self.result.append(self.find_median())
                to_remove = idx - k + 1
                if self.large and nums[to_remove] >= self.large[0]:
                    self.remove_element(self.large, nums[to_remove])
                else:
                    self.remove_element(self.small, -nums[to_remove])

        return self.result

def main():

    slidingWindowMedian = SlidingWindowMedian()
    result = slidingWindowMedian.find_sliding_window_median(
        [1], 1)
    print("Sliding window medians are: " + str(result))

    slidingWindowMedian = SlidingWindowMedian()
    result = slidingWindowMedian.find_sliding_window_median(
        [1, 2, -1, 3, 5], 3)
    print("Sliding window medians are: " + str(result))


main()
