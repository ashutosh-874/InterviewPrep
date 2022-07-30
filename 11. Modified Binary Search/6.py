# Problem Statement#

# Given an array of numbers sorted in ascending order, find the element in the array that has the minimum difference with the given ‘key’.

# Example 1:

# Input: [4, 6, 10], key = 7
# Output: 6
# Explanation: The difference between the key '7' and '6' is minimum than any other number in the array 

# Example 2:

# Input: [4, 6, 10], key = 4
# Output: 4

# Example 3:

# Input: [1, 3, 8, 10, 15], key = 12
# Output: 10

# Example 4:

# Input: [4, 6, 10], key = 17
# Output: 10


def search_min_diff_element(arr, key):

    n = len(arr)
    if arr[0] > key:
        return arr[0]
    elif arr[n-1] < key:
        return arr[n-1]

    l, r = 0, n - 1

    while l <= r:
        m = (l+r) // 2
        if arr[m] < key:
            l = m + 1
        elif arr[m] > key:
            r = m - 1
        else:
            return arr[m]
    
    if (arr[l] - key) < (key - arr[r]):
        return arr[l]
    return arr[r]


def main():
    print(search_min_diff_element([4, 6, 10], 7))
    print(search_min_diff_element([4, 6, 10], 4))
    print(search_min_diff_element([1, 3, 8, 10, 15], 12))
    print(search_min_diff_element([4, 6, 10], 17))


main()
