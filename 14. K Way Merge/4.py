# Problem Statement#

# Given ‘M’ sorted arrays, find the smallest range that includes at least one number from each of the ‘M’ lists.

# Example 1:

# Input: L1=[1, 5, 8], L2=[4, 12], L3=[7, 8, 10]
# Output: [4, 7]
# Explanation: The range [4, 7] includes 5 from L1, 4 from L2 and 7 from L3.

# Example 2:

# Input: L1=[1, 9], L2=[4, 12], L3=[7, 10, 16]
# Output: [9, 12]
# Explanation: The range [9, 12] includes 9 from L1, 12 from L2 and 10 from L3.


from heapq import heappop, heappush


def find_smallest_range(lists):

    min_heap = []
    res = None

    cur_max = -float('inf')
    for idx, lst in enumerate(lists):
        if lst[0] > cur_max: cur_max = lst[0]
        heappush(min_heap, (lst[0], idx, 0))
    res = (cur_max - min_heap[0][0], min_heap[0][0], cur_max)

    while min_heap:
        val, lst_idx, num_idx = heappop(min_heap)
        if num_idx == len(lists[lst_idx]) - 1:
            break
        nxt_el = lists[lst_idx][num_idx + 1]
        cur_max = max(cur_max, nxt_el)
        heappush(min_heap, (nxt_el, lst_idx, num_idx + 1))
        if cur_max - min_heap[0][0] < res[0]:
            res =  (cur_max - min_heap[0][0], min_heap[0][0], cur_max)

    print(res)
    
    return [res[1], res[2]]


def main():
    print("Smallest range is: " +
            str(find_smallest_range([[4,10,15,24,26],[0,9,12,20],[5,18,22,30]])))


main()

