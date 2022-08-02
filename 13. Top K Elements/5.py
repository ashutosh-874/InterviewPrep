# Problem Statement#

# Given an unsorted array of numbers, find the top ‘K’ frequently occurring numbers in it.

# Example 1:

# Input: [1, 3, 5, 12, 11, 12, 11], K = 2
# Output: [12, 11]
# Explanation: Both '11' and '12' apeared twice.

# Example 2:

# Input: [5, 12, 11, 3, 11], K = 2
# Output: [11, 5] or [11, 12] or [11, 3]
# Explanation: Only '11' appeared twice, all other numbers appeared once

from heapq import heapify, heappop, heappush


def find_k_frequent_numbers(nums, k):

    dct = {}
    for i in nums:
        dct[i] = dct.get(i, 0) + 1
    
    min_heap = []
    for key, value in dct.items():
        heappush(min_heap, (value, key))
        if len(min_heap) > k:
            heappop(min_heap)
    
    result = []
    while min_heap:
        result.append(heappop(min_heap)[1])
    
    return result
    




def main():

    # print("Here are the K frequent numbers: " +
    #         str(find_k_frequent_numbers([1, 3, 5, 3, 5, 3, 5, 3, 5, 3, 5, 3, 5, 3, 5, 3, 5, 3, 5, 3, 5, 3, 5, 3, 5, 3, 5, 12, 11, 12, 11, 11, 12, 11, 11, 12, 11, 11, 12, 11, 11, 12, 11], 2)))

    print("Here are the K frequent numbers: " +
            str(find_k_frequent_numbers([4,1,-1,2,-1,2,3], 2)))


main()

