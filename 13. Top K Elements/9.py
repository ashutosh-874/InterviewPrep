# Problem Statement#

# Given an array of numbers and a number ‘K’, we need to remove ‘K’ numbers from the array such that we are left with maximum distinct numbers.

# Example 1:

# Input: [7, 3, 5, 8, 5, 3, 3], and K=2
# Output: 3
# Explanation: We can remove two occurrences of 3 to be left with 3 distinct numbers [7, 3, 8], we have to skip 5 because it is not distinct and appeared twice. 

# Another solution could be to remove one instance of '5' and '3' each to be left with three distinct numbers [7, 5, 8], in this case, we have to skip 3 because it appeared twice.

# Example 2:

# Input: [3, 5, 12, 11, 12], and K=3
# Output: 2
# Explanation: We can remove one occurrence of 12, after which all numbers will become distinct. Then we can delete any two numbers which will leave us 2 distinct numbers in the result.

# Example 3:

# Input: [1, 2, 3, 3, 3, 3, 4, 4, 5, 5, 5], and K=2
# Output: 3
# Explanation: We can remove one occurrence of '4' to get three distinct numbers.


from heapq import heappop, heappush


def find_maximum_distinct_elements(nums, k):

    dct = {}
    for num in nums:
        dct[num] = dct.get(num, 0) + 1
    
    max_heap = []
    for key, value in dct.items():
        heappush(max_heap, (-value, key))

    print(max_heap)
    
    res = 0
    rem = k
    while max_heap:
        el = heappop(max_heap)
        print(el)
        if -el[0] > 1 and rem > 0:
            rem -= -el[0] - 1
            res += 1
        elif el[0] == -1:
            res += 1
        print(res, rem)
    
    if res > k:
        res = res - rem
    return res







def main():

    print("Maximum distinct numbers after removing K numbers: " +
            str(find_maximum_distinct_elements([7, 3, 5, 8, 5, 3, 3], 2)))
    print("Maximum distinct numbers after removing K numbers: " +
            str(find_maximum_distinct_elements([3, 5, 12, 11, 12], 3)))
    print("Maximum distinct numbers after removing K numbers: " +
            str(find_maximum_distinct_elements([1, 2, 3, 3, 3, 3, 4, 4, 5, 5, 5], 2)))


main()




# solution needs to be reviewed