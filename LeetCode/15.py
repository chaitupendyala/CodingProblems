'''
3Sum Given an integer array nums, return all the 
triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

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
	def threeSum(self, nums: List[int]) -> List[List[int]]:
		pass

s = Solution()
print("[-1,0,1,2,-1,-4]: " + s.threeSum([-1,0,1,2,-1,-4]))
print("[0]: " + s.threeSum())
