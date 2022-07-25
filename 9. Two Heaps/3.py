from heapq import *


def find_maximum_capital(capital, profits, k, w):

    cap_min_heap = []
    pro_max_heap = []

    for i in range(len(capital)):
        heappush(cap_min_heap, (capital[i], i))
    print(cap_min_heap)

    for _ in range(k):

        max_profit = 0
        while cap_min_heap and cap_min_heap[0][0] <= w:
            max_profit = max(max_profit, profits[heappop(cap_min_heap)[1]])
        if max_profit == 0:
            break

        heappush(pro_max_heap, -max_profit)
        w += max_profit

    return w    


    


def main():

    print("Maximum capital: " +
        str(find_maximum_capital([0, 1, 2], [1, 2, 3], 2, 1)))
    print("Maximum capital: " +
        str(find_maximum_capital([1, 1, 2, 3], [1, 2, 3, 5], 3, 0)))


main()
