'''
33. Search in Rotated Sorted Array

There is an integer array nums sorted in ascending order (with distinct values). Prior to being
passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k <
nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums
[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3
and become [4,5,6,7,0,1,2]. Given the array nums after the possible rotation and an integer target,
return the index of target if it is in nums, or -1 if it is not in nums. You must write an
algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Example 3:
Input: nums = [1], target = 0
Output: -1
'''
class Solution:
	def search(self, nums: list[int], target: int) -> int:
		index_of_target = -1
		found_target = False
		start = 0; end = len(nums) - 1
		while ( start <= end and not found_target ):
			middle = (start + end)//2
			if ( target == nums[middle] ):
				found_target = True
				index_of_target = middle

			if ( nums[middle] >= nums[start] ):
				if ( nums[start] <= target < nums[middle] ):
					end = middle - 1
				else: 
					start = middle + 1
			else:
				if ( nums[middle] < target <= nums[end] ):
					start = middle + 1
				else:
					end = middle - 1
		return index_of_target

print( "[4,5,6,7,0,1,2], target = 0: ", Solution().search([4,5,6,7,0,1,2], 0) )
print( "[4,5,6,7,0,1,2], target = 3: ", Solution().search([4,5,6,7,0,1,2], 3) )
print( "[1], target = 0: ", Solution().search([1], 0) )
print( "[1,3], target = 0: ", Solution().search([1,3], 0) )
print( "[1,3], target = 3: ", Solution().search([1,3], 3) )
print( "[3,1], target = 1: ", Solution().search([3,1], 1) )