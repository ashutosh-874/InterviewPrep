# Problem Statement#

# Given an array, find the sum of all numbers between the K1’th and K2’th smallest elements of that array.

# Example 1:

# Input: [1, 3, 12, 5, 15, 11], and K1=3, K2=6
# Output: 23
# Explanation: The 3rd smallest number is 5 and 6th smallest number 15. The sum of numbers coming
# between 5 and 15 is 23 (11+12).

# Example 2:

# Input: [3, 5, 8, 7], and K1=1, K2=4
# Output: 12
# Explanation: The sum of the numbers between the 1st smallest number (3) and the 4th smallest 
# number (8) is 12 (5+7).


from heapq import heapify, heappop, heappush


def find_sum_of_elements(nums, k1, k2):

    heapify(nums)

    c = 1
    res = 0
    while nums and c < k2:
        x = heappop(nums)
        if c > k1 and c < k2:
            res += x
        c += 1

    return res



def main():

    print("Sum of all numbers between k1 and k2 smallest numbers: " +
            str(find_sum_of_elements([1, 3, 12, 5, 15, 11], 3, 6)))
    print("Sum of all numbers between k1 and k2 smallest numbers: " +
            str(find_sum_of_elements([3, 5, 8, 7], 1, 4)))


main()
