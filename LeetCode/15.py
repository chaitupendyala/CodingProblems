'''
15. 3Sum

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that 
i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Example 2:

Input: nums = []
Output: []
Example 3:

Input: nums = [0]
Output: []
'''
class Solution:
	def threeSum(self, nums: list[int]) -> list[list[int]]:
		differences = {}
		return_list = []
		for i in range(len(nums)):
			differences = dict()
			difference = 0 - (nums[i])
			sum3 = list()
			for j in range(len(nums)):
				if i == j:
					pass
				diff = difference - nums[j]
				if diff in differences:
					sum3 = [nums[i], nums[j], differences[diff]]
					return_list.append(sum3)
				else:
					differences[diff] = nums[j]
		return return_list

print("nums = [-1,0,1,2,-1,-4]: ", Solution().threeSum([-1,0,1,2,-1,-4]))
print("nums = []: ", Solution().threeSum([]))
print("nums = [0]: ", Solution().threeSum([0]))