# Scheduling Tasks (hard)#

# You are given a list of tasks that need to be run, in any order, on a server. Each task will take one CPU interval to execute but once a task has finished, it has a cooling period during which it can’t be run again. If the cooling period for all tasks is ‘K’ intervals, find the minimum number of CPU intervals that the server needs to finish all tasks.

# If at any time the server can’t execute any task then it must stay idle.

# Example 1:

# Input: [a, a, a, b, c, c], K=2
# Output: 7
# Explanation: a -> c -> b -> a -> c -> idle -> a

# Example 2:

# Input: [a, b, a], K=3
# Output: 5
# Explanation: a -> b -> idle -> idle -> a

from collections import Counter
from heapq import heapify, heappop, heappush


def schedule_tasks(tasks, k):
    count = Counter(tasks)
    max_heap = [(-cnt, chr) for chr, cnt in count.items()]

    heapify(max_heap)

    res = ""
    temp = []
    items_added = 0
    chars_added = 0
    while max_heap:
        item = heappop(max_heap)
        res += item[1]
        chars_added += 1
        items_added += 1
        if item[0] < -1:
            temp.append((item[0] + 1, item[1]))
        # while items_added <= k:
        #     res += "-"
        #     items_added += 1
        if items_added > k:
            for x in temp: heappush(max_heap, x)
            temp = []
            items_added = 0
        elif not max_heap and items_added <= k:
            while items_added <= k and chars_added < len(tasks):
                res += "-"
                items_added += 1
            for x in temp: heappush(max_heap, x)
            temp = []
            items_added = 0

    # print(res)
    return len(res)


def main():
    print("Minimum intervals needed to execute all tasks: " +
            str(schedule_tasks(["A","A","A","B","B","B"], 2)))
    print("Minimum intervals needed to execute all tasks: " +
            str(schedule_tasks(["A","A","A","A","A","A","B","C","D","E","F","G"], 2)))
    print("Minimum intervals needed to execute all tasks: " +
            str(schedule_tasks(["A","A","A","B","B","B"], 0)))


main()

