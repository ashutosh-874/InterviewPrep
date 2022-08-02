# Rearrange String K Distance Apart (hard)#

# Given a string and a number ‘K’, find if the string can be rearranged such that the same characters are at least ‘K’ distance apart from each other.

# Example 1:

# Input: "mmpp", K=2
# Output: "mpmp" or "pmpm"
# Explanation: All same characters are 2 distance apart.

# Example 2:

# Input: "Programming", K=3
# Output: "rgmPrgmiano" or "gmringmrPoa" or "gmrPagimnor" and a few more
# Explanation: All same characters are 3 distance apart.

# Example 3:

# Input: "aab", K=2
# Output: "aba"
# Explanation: All same characters are 2 distance apart.

# Example 4:

# Input: "aappa", K=3
# Output: ""
# Explanation: We cannot find an arrangement of the string where any two 'a' are 3 distance apart.


from collections import Counter
from heapq import heapify, heappop, heappush


def reorganize_string(str, k):

    count = Counter(str)
    max_heap = [(-count, char) for char, count in count.items()]

    heapify(max_heap)

    temp = []
    res = ""
    while max_heap:
        item = heappop(max_heap)
        res += item[1]
        if item[0] < -1:
            temp.append((item[0] + 1, item[1]))
        if len(temp) >= k or (not max_heap and temp and temp[0][0] == -1) :
            for x in temp: heappush(max_heap, x)
            temp = [] 
    
    return res if len(res) == len(str) else ""



def main():
    # print("Reorganized string: " + reorganize_string("mmpp", 2))
    # print("Reorganized string: " + reorganize_string("Programming", 3))
    # print("Reorganized string: " + reorganize_string("aab", 2))
    # print("Reorganized string: " + reorganize_string("aapa", 3))
    print("Reorganized string: " + reorganize_string("aaadbbcc", 2))


main()
