# Problem Statement#

# Given a sorted number array and two integers ‘K’ and ‘X’, find ‘K’ closest numbers to ‘X’ in the array. Return the numbers in the sorted order. ‘X’ is not necessarily present in the array.

# Example 1:

# Input: [5, 6, 7, 8, 9], K = 3, X = 7
# Output: [6, 7, 8]

# Example 2:

# Input: [2, 4, 5, 6, 9], K = 3, X = 6
# Output: [4, 5, 6]

# Example 3:

# Input: [2, 4, 5, 6, 9], K = 3, X = 10
# Output: [5, 6, 9]

from heapq import heappop, heappush

def binary_search(arr, target):
    l, r = 0, len(arr) - 1
    while l < r:
        m = (l+r) // 2
        if arr[m] == target:
            return m
        elif arr[m] < target:
            l = m + 1
        else:
            r = m - 1
    if l > 0:
        return l - 1
    else: return l

def find_closest_elements(arr, k, x):
    idx = binary_search(arr, x)
    low, high = idx - k, idx + k
    low = max(low, 0)
    high = min(high, len(arr) - 1)

    min_heap = []
    for i in range(low, high+1):
        heappush(min_heap, (abs(arr[i] - x), arr[i]))
    
    result = []
    for _ in range(k):
        result.append(heappop(min_heap)[1])

    result.sort()
    return result







def main():
    print("'K' closest numbers to 'X' are: " +
            str(find_closest_elements([1, 2, 3, 4, 5], 4, 3)))
    print("'K' closest numbers to 'X' are: " +
            str(find_closest_elements([2, 4, 5, 6, 9], 3, 6)))
    print("'K' closest numbers to 'X' are: " +
            str(find_closest_elements([2, 4, 5, 6, 9], 3, 10)))


main()
