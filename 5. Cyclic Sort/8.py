# Find the First K Missing Positive Numbers (hard)#

# Given an unsorted array containing numbers and a number ‘k’, find the first ‘k’ missing positive numbers in the array.

# Example 1:

# Input: [3, -1, 4, 5, 5], k=3
# Output: [1, 2, 6]
# Explanation: The smallest missing positive numbers are 1, 2 and 6.

# Example 2:

# Input: [2, 3, 4], k=3
# Output: [1, 5, 6]
# Explanation: The smallest missing positive numbers are 1, 5 and 6.

# Example 3:

# Input: [-2, -3, 4], k=2
# Output: [1, 2]
# Explanation: The smallest missing positive numbers are 1 and 2.


def find_first_k_missing_positive(nums, k):
    missingNumbers = []

    i, n = 0, len(nums)
    while i < len(nums):
        j = nums[i] - 1
        if nums[i] > 0 and nums[i] <= n and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1

    # print(nums)

    extraNumbers = set()
    i = 0
    while k > 0:
        if i < n:
            if nums[i] != i + 1:
                missingNumbers.append(i+1)
                k -= 1
                if nums[i] > 0:
                    extraNumbers.add(nums[i])
        else:
            if (i+1) not in extraNumbers:
                missingNumbers.append(i+1)
                k -= 1
        
        i += 1


    return missingNumbers


print(find_first_k_missing_positive([-2, -3, 4], 8))
print(find_first_k_missing_positive([2, 3, 4], 3))
print(find_first_k_missing_positive([2, 3, 4, 1], 3))