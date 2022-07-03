# Problem Statement#

# Given two lists of intervals, find the intersection of these two lists. Each list consists of disjoint intervals sorted on their start time.

# Example 1:

# Input: arr1=[[1, 3], [5, 6], [7, 9]], arr2=[[2, 3], [5, 7]]
# Output: [2, 3], [5, 6], [7, 7]
# Explanation: The output list contains the common intervals between the two lists.

# Example 2:

# Input: arr1=[[1, 3], [5, 7], [9, 12]], arr2=[[5, 10]]
# Output: [5, 7], [9, 10]
# Explanation: The output list contains the common intervals between the two lists.


def merge(firstList, secondList):
    result = []

    x, y = 0, 0
    while x < len(firstList) and y < len(secondList):
        
        if firstList[x][1] < secondList[y][0]:
            x += 1
        elif firstList[x][0] > secondList[y][1]:
            y += 1
        else:
            result.append([max(firstList[x][0], secondList[y][0]), min(firstList[x][1], secondList[y][1])])
            if firstList[x][1] < secondList[y][1]:
                x += 1
            elif firstList[x][1] > secondList[y][1]:
                y += 1
            else:
                x += 1
                y += 1


    return result


def main():
    print("Intervals Intersection: " + str(merge([[0,2],[5,10],[13,23],[24,25]], [[1,5],[8,12],[15,24],[25,26]])))
    print("Intervals Intersection: " + str(merge([[1,3],[5,9]], [])))


main()
