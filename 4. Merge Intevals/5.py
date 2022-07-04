# Minimum Meeting Rooms (hard)#

# Given a list of intervals representing the start and end time of ‘N’ meetings, find the minimum number of rooms required to hold all the meetings.

# Example 1:

# Meetings: [[1,4], [2,5], [7,9]]
# Output: 2
# Explanation: Since [1,4] and [2,5] overlap, we need two rooms to hold these two meetings. [7,9] can 
# occur in any of the two rooms later.

# Example 2:

# Meetings: [[6,7], [2,4], [8,12]]
# Output: 1
# Explanation: None of the meetings overlap, therefore we only need one room to hold all meetings.

# Example 3:

# Meetings: [[1,4], [2,3], [3,6]]
# Output:2
# Explanation: Since [1,4] overlaps with the other two meetings [2,3] and [3,6], we need two rooms to 
# hold all the meetings.

# Example 4:

# Meetings: [[4,5], [2,3], [2,4], [3,5]]
# Output: 2
# Explanation: We will need one room for [2,3] and [3,5], and another room for [2,4] and [4,5].

# Here is a visual representation of Example 4:

def min_meeting_rooms(A):

    starts = sorted([x[0] for x in A])
    ends = sorted([y[1] for y in A])

    x, y = 0, 0
    ans, cur_meetings = 0, 0

    while x < len(starts):
        if starts[x] < ends[y]:
            cur_meetings += 1
            x += 1
        else:
            cur_meetings -= 1
            y += 1
        ans = max(ans, cur_meetings)

    return ans


def main():

    print(min_meeting_rooms([
        [4, 10],
        [22, 26],
        [22, 28],
        [24, 26],
        [13, 19],
        [6, 27],
        [10, 26],
        [23, 29],
        [8, 22],
        [10, 11],
        [12, 21],
    ]))


main()




