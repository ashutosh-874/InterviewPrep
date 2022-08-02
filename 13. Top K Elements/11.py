# Problem Statement#

# Given a string, find if its letters can be rearranged in such a way that no two same characters come next to each other.

# Example 1:

# Input: "aappp"
# Output: "papap"
# Explanation: In "papap", none of the repeating characters come next to each other.

# Example 2:

# Input: "Programming"
# Output: "rgmrgmPiano" or "gmringmrPoa" or "gmrPagimnor", etc.
# Explanation: None of the repeating characters come next to each other.

# Example 3:

# Input: "aapa"
# Output: ""
# Explanation: In all arrangements of "aapa", atleast two 'a' will come together e.g., "apaa", "paaa".

from heapq import *


def rearrange_string(str):

    dct = {}
    for i in str:
        dct[i] = dct.get(i, 0) + 1
    
    max_heap = []
    for key, val in dct.items():
        heappush(max_heap, (-val, key))

    res = ""
    temp = []
    while max_heap:
        item = heappop(max_heap)
        res += item[1]
        if -item[0] > 1:
            temp.append((item[0]+1, item[1]))
        if len(temp) == 2 or not max_heap or not -item[0] > 1:
            for x in temp: heappush(max_heap, x)
            temp = []
    
    if res[-2] == res[-1]:
        return ""
    return res


        
    



def main():
    print("Rearranged string:  " + rearrange_string("baaba"))
    print("Rearranged string:  " + rearrange_string("Programming"))
    print("Rearranged string:  " + rearrange_string("aaab"))
    print("Rearranged string:  " + rearrange_string("vvvlo"))


main()

