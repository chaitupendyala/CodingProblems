'''
16. 3Sum Closest
Medium

Given an integer array nums of length n and an integer target, 
find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

Example 1:
Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

Example 2:
Input: nums = [0,0,0], target = 1
Output: 0

Constraints:

3 <= nums.length <= 1000
-1000 <= nums[i] <= 1000
-10^4 <= target <= 10^4
'''
class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        result = sum(nums[:3])

        for i in range(len(nums)):
            l, r = i+1, len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s == target:
                    return s
                if abs(s - target) < abs(result - target):
                    result = s
                
                if s < target:
                    l += 1
                elif s > target:
                    r -= 1
        return result

print("nums = [-1,2,1,-4], target = 1:", Solution().threeSumClosest(nums = [-1,2,1,-4], target = 1)) #Output: 2
print("nums = [0,0,0], target = 1:", Solution().threeSumClosest(nums = [0,0,0], target = 1)) #Output: 0
print("nums = [1,1,1,0], target = -100:", Solution().threeSumClosest(nums = [1,1,1,0], target = -100)) #Output: 2