# Problem Statement#

# Given a list of intervals, merge all the overlapping intervals to produce a list that has only mutually exclusive intervals.

# Example 1:

# Intervals: [[1,4], [2,5], [7,9]]
# Output: [[1,5], [7,9]]
# Explanation: Since the first two intervals [1,4] and [2,5] overlap, we merged them into 
# one [1,5].

# Example 2:

# Intervals: [[6,7], [2,4], [5,9]]
# Output: [[2,4], [5,9]]
# Explanation: Since the intervals [6,7] and [5,9] overlap, we merged them into one [5,9].

# Example 3:

# Intervals: [[1,4], [2,6], [3,5]]
# Output: [[1,6]]
# Explanation: Since all the given intervals overlap, we merged them into one.

class Interval:
	def __init__(self, start, end):
		self.start = start
		self.end = end

	def print_interval(self):
		print("[" + str(self.start) + ", " + str(self.end) + "]", end='')

def merge(intervals):
	merged = [intervals[0]]
	
	intervals.sort(key = lambda x: x.start)

	for interval in intervals[1:]:
		
		cur = merged[-1]
		if interval.start <= cur.end and interval.end >= cur.end:
			merged.pop()
			merged.append(Interval(cur.start, interval.end))
		elif interval.start > cur.end:
			merged.append(interval)
			
	return merged


def main():
	print("Merged intervals: ", end='')
	for i in merge([Interval(1, 4), Interval(2, 5), Interval(7, 9)]):
		i.print_interval()
	print()

	print("Merged intervals: ", end='')
	for i in merge([Interval(6, 7), Interval(2, 4), Interval(5, 9)]):
		i.print_interval()
	print()

	print("Merged intervals: ", end='')
	for i in merge([Interval(1, 4), Interval(2, 6), Interval(3, 5)]):
		i.print_interval()
	print()

main()