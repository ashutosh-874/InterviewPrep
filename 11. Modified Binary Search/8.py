# Search Bitonic Array (medium)#

# Given a Bitonic array, find if a given ‘key’ is present in it. An array is considered bitonic if it is monotonically increasing and then monotonically decreasing. Monotonically increasing or decreasing means that for any index i in the array arr[i] != arr[i+1].

# Write a function to return the index of the ‘key’. If the ‘key’ is not present, return -1.

# Example 1:

# Input: [1, 3, 8, 4, 3], key=4
# Output: 3

# Example 2:

# Input: [10, 8, 7, 1], key=10
# Output: 1

# Example 3:

# Input: [1, 3, 8, 12], key=12
# Output: 3

# Example 4:

# Input: [10, 9, 8], key=10
# Output: 0


def find_max_in_bitonic_array(arr):
    l, r= 0, len(arr) - 1
    while l < r:
        m = (l+r) // 2
        if arr[m] <= arr[m+1]:
            l = m + 1
        else:
            r = m
    return l

def find_key_in_asc(arr, key):
    l, r = 0, len(arr) - 1
    while l <= r:
        m = (l+r) // 2
        if arr[m] < key:
            l = m+1
        elif arr[m] > key:
            r = m - 1
        else:
            return m
    return -1

def find_key_in_dsc(arr, key):
    l, r = 0, len(arr) - 1
    while l <= r:
        m = (l+r) // 2
        if arr[m] < key:
            r = m - 1
        elif arr[m] > key:
            l = m + 1
        else:
            return m
    return -1

def search_bitonic_array(arr, key):
    mx = find_max_in_bitonic_array(arr)
    if arr[mx] == key: return mx
    else:
        lft = find_key_in_asc(arr[:mx+1], key)
        rgt = mx + 1 + find_key_in_dsc(arr[mx+1:], key)
        if lft != -1:
            return lft
        if rgt != -1:
            return rgt
        return -1


def main():
    print(search_bitonic_array([1, 3, 8, 4, 3], 4))
    print(search_bitonic_array([3, 8, 3, 1], 8))
    print(search_bitonic_array([1, 3, 8, 12], 12))
    print(search_bitonic_array([10, 9, 8], 10))


main()
