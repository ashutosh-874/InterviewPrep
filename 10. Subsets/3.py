# Problem Statement#

# Given a set of distinct numbers, find all of its permutations.

# Permutation is defined as the re-arranging of the elements of the set. For example, {1, 2, 3} has the following six permutations:

#     {1, 2, 3}
#     {1, 3, 2}
#     {2, 1, 3}
#     {2, 3, 1}
#     {3, 1, 2}
#     {3, 2, 1}

# If a set has ‘n’ distinct elements it will have n!n!n! permutations.

# Example 1:

# Input: [1,3,5]
# Output: [1,3,5], [1,5,3], [3,1,5], [3,5,1], [5,1,3], [5,3,1]


def find_permutations(nums):

    if not nums:
        return nums

    results = [[]]

    for num in nums:
        new_results = []
        for result in results:
            ln = len(result)
            for i in range(ln + 1):
                result_copy = result[:]
                result_copy.insert(i, num)
                new_results.append(result_copy)
        results = new_results

    return results

    


def main():
    print("Here are all the permutations: " + str(find_permutations([5, 5,5, 5])))


main()
