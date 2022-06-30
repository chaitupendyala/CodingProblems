'''
57. Insert Interval

You are given an array of non-overlapping intervals intervals where intervals
[i] = [starti, endi] represent the start and the end of the ith interval and
intervals is sorted in ascending order by starti. You are also given an
interval newInterval = [start, end] that represents the start and end of
another interval.

Insert newInterval into intervals such that intervals is still sorted in
ascending order by starti and intervals still does not have any overlapping
intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

Example 1:
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Example 2:
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
'''
class Solution:
	def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
		def sortSecond(val):
			return val[0]

		intervals.append(newInterval)

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

print("intervals = [[1,3],[6,9]], newInterval = [2,5]: ", Solution().insert([[1,3],[6,9]],[2,5]))
print("intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]: ", Solution().insert([[1,2],[3,5],[6,7],[8,10],[12,16]],[4,8]))