# Problem Statement#

# Given ‘M’ sorted arrays, find the K’th smallest number among all the arrays.

# Example 1:

# Input: L1=[2, 6, 8], L2=[3, 6, 7], L3=[1, 3, 4], K=5
# Output: 4
# Explanation: The 5th smallest number among all the arrays is 4, this can be verified from 
# the merged list of all the arrays: [1, 2, 3, 3, 4, 6, 6, 7, 8]

# Example 2:

# Input: L1=[5, 8, 9], L2=[1, 7], K=3
# Output: 7
# Explanation: The 3rd smallest number among all the arrays is 7.


from heapq import heappop, heappush


def find_Kth_smallest(lists, k):

    min_heap = []
    for idx, lst in enumerate(lists):
        heappush(min_heap, (lst[0], idx, 0))
    
    print(min_heap)
    for i in range(k):
        el = heappop(min_heap)
        if el[2]+1 < len(lists[el[1]]):
            heappush(min_heap, (lists[el[1]][el[2]+1], el[1], el[2]+1))
        print(min_heap)
    
    return el[0]
    


def main():
    print("Kth smallest number is: " +
            str(find_Kth_smallest([[-5]], 1)))
    print("Kth smallest number is: " +
            str(find_Kth_smallest([[1,5,9],[10,11,13],[12,13,15]], 8)))


main()
