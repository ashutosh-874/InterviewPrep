# Find the Smallest Missing Positive Number (medium)#

# Given an unsorted array containing numbers, find the smallest missing positive number in it.

# Note: Positive numbers start from ‘1’.

# Example 1:

# Input: [-3, 1, 5, 4, 2]
# Output: 3
# Explanation: The smallest missing positive number is '3'

# Example 2:

# Input: [3, -2, 0, 1, 2]
# Output: 4

# Example 3:

# Input: [3, 2, 5, 1]
# Output: 4


def find_first_smallest_missing_positive(nums):


    # my approach

    # n = len(nums)

    # l_0_count = 0
    # for i in nums:
    #     if i <= 0: l_0_count += 1

    # j = l_0_count
    # for i in range(n):
    #     if nums[i] <= 0:
    #         nums[i], nums[l_0_count - j] = nums[l_0_count - j], nums[i]
    #         j -= 1


    # i = 0
    # while i < (n - l_0_count):
    #     x = i + l_0_count
    #     y = nums[i + l_0_count] + l_0_count - 1
    #     if y < n and nums[x] != nums[y]:
    #         nums[x], nums[y] = nums[y], nums[x]
    #     else:
    #         i += 1

    # for i in range(0, n + 1):
    #     try:
    #         if nums[i + l_0_count] != i+1:
    #             return i+1
    #     except IndexError:
    #         return n - l_0_count + 1


    # solution
    i = 0
    n = len(nums)
    while i < n:
        j = nums[i] - 1
        if nums[i] > 0 and nums[i] <= n and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1


    for i in range(n):
        if nums[i] != i + 1:
            return i + 1

    return len(nums) + 1







print(find_first_smallest_missing_positive([3, 0, 1, 2]))
print(find_first_smallest_missing_positive([2, 3, 4]))