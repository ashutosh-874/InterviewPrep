# Problem Statement#

# Given a set of numbers that might contain duplicates, find all of its distinct subsets.

# Example 1:

# Input: [1, 3, 3]
# Output: [], [1], [3], [1,3], [3,3], [1,3,3]

# Example 2:

# Input: [1, 5, 3, 3]
# Output: [], [1], [5], [3], [1,5], [1,3], [5,3], [1,5,3], [3,3], [1,3,3], [3,3,5], [1,5,3,3] 

def find_subsets(nums):
    nums.sort()
    subsets = []
    subsets.append([])

    for i in range(len(nums)):
        ln = len(subsets)
        if not (i >= 1 and nums[i] == nums[i - 1]):
            y = 0
        while y < ln:
            x = subsets[y][:]
            x.append(nums[i])
            subsets.append(x)
            y += 1
        
    return subsets


def main():

    # print(str(find_subsets([1, 1, 1])))
    print(str(find_subsets([1, 5, 3, 3])))


main()
