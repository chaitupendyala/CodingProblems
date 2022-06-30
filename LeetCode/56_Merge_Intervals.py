'''
56. Merge Intervals

Given an array of intervals where intervals[i] = [starti, endi], merge all
overlapping intervals, and return an array of the non-overlapping intervals
that cover all the intervals in the input.

Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
'''
class Solution:
	def merge(self, intervals: list[list[int]]) -> list[list[int]]:
		def sortSecond(val):
			return val[0]

		intervals.sort(key= sortSecond)
		merged_intervals = []
		current_interval = intervals[0]

		for i in range(1, len(intervals)):
			if intervals[i][0] > current_interval[1]:
				merged_intervals.append(current_interval)
				current_interval = intervals[i]
				continue

			current_interval = [min(intervals[i][0], current_interval[0]),max(intervals[i][1],current_interval[1])]
		merged_intervals.append(current_interval)
		return merged_intervals


print("intervals = [[1,3],[2,6],[8,10],[15,18]]: ", Solution().merge([[1,3],[2,6],[8,10],[15,18]]))
print("intervals = [[1,4],[4,5]]: ", Solution().merge([[1,4],[4,5]]))