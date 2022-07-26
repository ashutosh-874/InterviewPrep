# Problem Statement#

# Given a set with distinct elements, find all of its distinct subsets.

# Example 1:

# Input: [1, 3]
# Output: [], [1], [3], [1,3]

# Example 2:

# Input: [1, 5, 3]
# Output: [], [1], [5], [3], [1,5], [1,3], [5,3], [1,5,3]

def find_subsets(nums):
    subsets = []
    subsets.append([])

    for i in nums:
        ln = len(subsets)
        for y in range(ln):
            x = subsets[y][:]
            x.append(i)
            subsets.append(x)
        
    return subsets


def main():

    print("Here is the list of subsets: " + str(find_subsets([1, 3])))
    print("Here is the list of subsets: " + str(find_subsets([1, 5, 3])))


main()
