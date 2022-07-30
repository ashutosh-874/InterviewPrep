# Problem Statement#

# Given an array of numbers sorted in ascending order, find the range of a given number ‘key’. The range of the ‘key’ will be the first and last position of the ‘key’ in the array.

# Write a function to return the range of the ‘key’. If the ‘key’ is not present return [-1, -1].

# Example 1:

# Input: [4, 6, 6, 6, 9], key = 6
# Output: [1, 3]

# Example 2:

# Input: [1, 3, 8, 10, 15], key = 10
# Output: [3, 3]

# Example 3:

# Input: [1, 3, 8, 10, 15], key = 12
# Output: [-1, -1]

# def find_starting_idx(arr, target):

#     l, r = 0, len(arr) - 1

#     while l <= r:
#         m = (l+r) // 2
#         if l==r==m:
#             return m
#         if arr[m] == target:
#             r = m
#         else:
#             l = m + 1


# def find_end_idx(arr, target):
#     l, r = 0, len(arr) - 1
#     while l <= r:
#         m = ((l+r) // 2) + 1
#         if l==r==m:
#             return m
#         if  m > r:
#             return m - 1
#         if arr[m] > target:
#             r = m - 1
#         else:
#             l = m


# def find_range(arr, target):
#     result = [- 1, -1]

#     l, r = 0, len(arr) - 1

#     while l <= r:
#         m = (l+r) // 2
#         if arr[m] == target:
#             return [find_starting_idx(arr[:m+1], target), m + find_end_idx(arr[m:], target)]
#         elif arr[m] < target:
#             l = m + 1
#         else:
#             r = m - 1

#     return result

def find_range(arr, target):
    result = [-1, -1]
    result[0] = mbfs(arr, target, False)
    if result[0] != -1:
        result[1] = mbfs(arr, target, True)
    return result


def mbfs(arr, target, checkEndIdx):
    l, r = 0, len(arr) - 1
    key_idx = -1
    while l <= r:
        m = (l+r) // 2
        if arr[m] < target:
            l = m + 1
        elif arr[m] > target:
            r = m - 1
        else:
            key_idx = m
            if checkEndIdx:
                l = m + 1
            else:
                r = m - 1
            
    return key_idx



def main():
    print(find_range([4, 6, 6, 6, 9], 6))
    print(find_range([1, 3, 8, 10, 15], 10))
    print(find_range([1, 3, 8, 10, 15], 12))


main()
