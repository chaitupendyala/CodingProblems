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

'''
a+b=-c, 3SUM can be reduced to a 2SUM problem
'''
class Solution:
	def threeSum(self, nums: list[int]) -> list[list[int]]:
		nums.sort()
		n, results = len(nums), []

		for index in range(n):
			if index > 0 and nums[index] == nums[index-1]:
				continue
			target = 0 - nums[index]
			start,end = index+1, n-1

			while start<end:
				if nums[start] + nums[end] == target:
					results.append([nums[index], nums[start], nums[end]])
					start += 1
					while start<end and nums[start] == nums[start-1]:
						start+=1
				elif nums[start] + nums[end] < target:
					start+=1
				else:
					end-=1
		return results

print("nums = [-1,0,1,2,-1,-4]: ", Solution().threeSum([-1,0,1,2,-1,-4]))
print("nums = []: ", Solution().threeSum([]))
print("nums = [0]: ", Solution().threeSum([0]))