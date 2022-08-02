# Problem Statement#

# Given a string, sort it based on the decreasing frequency of its characters.

# Example 1:

# Input: "Programming"
# Output: "rrggmmPiano"
# Explanation: 'r', 'g', and 'm' appeared twice, so they need to appear before any other character.

# Example 2:

# Input: "abcbab"
# Output: "bbbaac"
# Explanation: 'b' appeared three times, 'a' appeared twice, and 'c' appeared only once.

from heapq import heappop, heappush


def sort_character_by_frequency(str):
    
    dct = {}
    for i in str:
        dct[i] = dct.get(i, 0) + 1
    
    min_heap = []
    for key, value in dct.items():
        heappush(min_heap, (value, key))
    
    res = ""
    while min_heap:
        x = heappop(min_heap)
        res = x[1]*x[0] + res
    
    return res


def main():

    print("String after sorting characters by frequency: " +
            sort_character_by_frequency("Programming"))
    print("String after sorting characters by frequency: " +
            sort_character_by_frequency("abcbab"))


main()
