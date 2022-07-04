# Employee Free Time (hard)#

# For ‘K’ employees, we are given a list of intervals representing the working hours of each employee. Our goal is to find out if there is a free interval that is common to all employees. You can assume that each list of employee working hours is sorted on the start time.

# Example 1:

# Input: Employee Working Hours=[[[1,3], [5,6]], [[2,3], [6,8]]]Output: [3,5]Explanation: Both the employees are free between [3,5].

# Example 2:

# Input: Employee Working Hours=[[[1,3], [9,12]], [[2,4]], [[6,8]]]Output: [4,6], [8,9]Explanation: All employees are free between [4,6] and [8,9].

# Example 3:

# Input: Employee Working Hours=[[[1,3]], [[2,4]], [[3,5], [7,9]]]Output: [5,7]Explanation: All employees are free between [5,7].


from __future__ import print_function

class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def print_interval(self):
        print("[" + str(self.start) + ", " + str(self.end) + "]", end='')


def find_employee_free_time(schedule):
    result = []
    
    new_schedule = []
    for x in schedule:
        for i in x:
            new_schedule.append(i)

    new_schedule.sort(key = lambda x: x.start)

    merged = [new_schedule[0]]
    for sch in new_schedule[1:]:

        cur = merged[-1]
        if sch.start > cur.end:
            merged.append(sch)
        else:
            merged.pop()
            merged.append(Interval(min(cur.start, sch.start), max(cur.end, sch.end)))
        
    if len(merged) <= 1: return result

    for i in range(1, len(merged)) :
        result.append(Interval(merged[i - 1].end, merged[i].start))

    return result


def main():

    input = [[Interval(1, 3), Interval(5, 6)], [
        Interval(2, 3), Interval(6, 8)]]
    print("Free intervals: ", end='')
    for interval in find_employee_free_time(input):
        interval.print_interval()
    print()

    input = [[Interval(1, 3), Interval(9, 12)], [
        Interval(2, 4)], [Interval(6, 8)]]
    print("Free intervals: ", end='')
    for interval in find_employee_free_time(input):
        interval.print_interval()
    print()

    input = [[Interval(1, 3)], [
        Interval(2, 4)], [Interval(3, 5), Interval(7, 9)]]
    print("Free intervals: ", end='')
    for interval in find_employee_free_time(input):
        interval.print_interval()
    print()


main()



# this solution needs to be reviewed