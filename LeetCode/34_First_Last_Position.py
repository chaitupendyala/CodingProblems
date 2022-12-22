'''
34. Find First and Last Position of Element in Sorted Array
Medium

Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]
'''
import bisect

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left_index, right_index = bisect.bisect_left(nums, target), bisect.bisect_right(nums, target)
        if left_index == right_index:
            return [-1,-1]
        else:
            return [left_index, right_index-1]