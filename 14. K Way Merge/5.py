# K Pairs with Largest Sums (Hard)#

# Given two sorted arrays in descending order, find ‘K’ pairs with the largest sum where each pair consists of numbers from both the arrays.

# Example 1:

# Input: L1=[9, 8, 2], L2=[6, 3, 1], K=3
# Output: [9, 3], [9, 6], [8, 6] 
# Explanation: These 3 pairs have the largest sum. No other pair has a sum larger than any of these.

# Example 2:

# Input: L1=[5, 2, 1], L2=[2, -1], K=3
# Output: [5, 2], [5, -1], [2, 2] 

from heapq import heappop, heappush


def find_k_largest_pairs(nums1, nums2, k):

    min_heap = []

    for num1 in nums1[:k]:
        for num2 in nums2[:k]:
            if len(min_heap) < k:
                heappush(min_heap, (num1+num2, num1, num2))
            else:
                if num1+num2 < min_heap[0][0]:
                    break
                else:
                    heappop(min_heap)
                    heappush(min_heap, (num1+num2, num1, num2))

    print(min_heap)
    res = []
    while min_heap:
        el = heappop(min_heap)
        res.append([el[1], el[2]])
    return res




def main():
    print("Pairs with largest sum are: " +
            str(find_k_largest_pairs([9, 8, 2], [6, 3, 1], 3)))


main()
