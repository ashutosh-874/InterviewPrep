# Problem Statement#

# We are given an unsorted array containing ‘n+1’ numbers taken from the range 1 to ‘n’. The array has only one duplicate but it can be repeated multiple times. Find that duplicate number without using any extra space. You are, however, allowed to modify the input array.

# Example 1:

# Input: [1, 4, 4, 3, 2]
# Output: 4

# Example 2:

# Input: [2, 1, 3, 3, 5, 4]
# Output: 3

# Example 3:

# Input: [2, 4, 1, 4, 4]
# Output: 4

def find_duplicate(nums):
    i = 0
    while i < len(nums):
        if nums[i] != i + 1:
            j = nums[i] - 1
            if nums[i] == nums[j]:
                return nums[i]
            else:
                nums[i], nums[j] = nums[j], nums[i]
        else:   
            i += 1

    return -1



print(find_duplicate([2, 4, 1, 4, 4]))
print(find_duplicate([2, 1, 3, 3, 5, 4]))
print(find_duplicate([1, 4, 4, 3, 2]))