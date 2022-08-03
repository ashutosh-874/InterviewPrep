# Problem Statement#

# Given an N∗NN * NN∗N matrix where each row and column is sorted in ascending order, find the Kth smallest element in the matrix.

# Example 1:

# Input: Matrix=[
#     [2, 6, 8], 
#     [3, 7, 10],
#     [5, 8, 11]
#   ], 
#   K=5
# Output: 7
# Explanation: The 5th smallest number in the matrix is 7.


from heapq import heappop, heappush


def find_Kth_smallest(matrix, k):

    min_heap = []
    n = len(matrix) - 1

    for idx, lst in enumerate(matrix):
        heappush(min_heap, (lst[0], idx, 0))
    print(min_heap)
    for _ in range(k):
        val, lst_idx, num_idx = heappop(min_heap)
        if num_idx <= n-1:
            heappush(min_heap, (matrix[lst_idx][num_idx+1], lst_idx, num_idx+1))
        print(min_heap)
    return val
        



def main():
  print("Kth smallest number is: " +
        str(find_Kth_smallest([[-5]], 1)))


main()
