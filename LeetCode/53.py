'''
53. Maximum Subarray

Given an integer array nums, find the contiguous subarray (containing at least one number) which has
the largest sum and return its sum. A subarray is a contiguous part of an array.

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Example 2:
Input: nums = [1]
Output: 1

Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23
'''
class Solution:
	def maxSubArray(self, nums: list[int]) -> int:
		len_of_nums = len(nums)
		OPT = [None for _ in range(len_of_nums)]
		OPT[0] = nums[0]
		for i in range(1, len_of_nums):
			OPT[i] = max(OPT[i-1] + nums[i], nums[i])
		return max(OPT)

print("nums = [-2,1,-3,4,-1,2,1,-5,4]: ", Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print("nums = [1]: ", Solution().maxSubArray([1]))
print("nums = [5,4,-1,7,8]: ", Solution().maxSubArray([5,4,-1,7,8]))