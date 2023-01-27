'''
128. Longest Consecutive Sequence
Medium

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

Constraints:
0 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
'''
class Solution:
	def longestConsecutive(self, nums: list[int]) -> int:
		# Convert the nums in to a set so that the retrieval becomes
		# O(1) instead of O(n)
		nums = set(nums)
		# The longest consecutive sequence in a array with no concecutive numbers is 1
		# But the list can also be empty in which case the longest consecutive sequence will be 0
		longest_consecutive = 0
		for num in nums:
			# Since nums is a set this check takes just O(1)
			# If the previous number is in nums we don't check it because in the below logic
			# we will check the number anyways
			if num - 1 not in nums:
				next_num = num + 1
				# We check if the next numbers is in the list or not. If they are we continue till we
				# don't find the number in the set anymore.
				while next_num in nums:
					next_num += 1
				# Since the numbers are consecutive next_num = num will return the length of numbers between
				# them
				longest_consecutive = max( longest_consecutive, next_num - num )
		return longest_consecutive

print("nums = [100,4,200,1,3,2]:", Solution().longestConsecutive([100,4,200,1,3,2]))
print("nums = [0,3,7,2,5,8,4,6,0,1]:", Solution().longestConsecutive([0,3,7,2,5,8,4,6,0,1]))