'''
213. House Robber II
Medium

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed.
All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one.
Meanwhile, adjacent houses have a security system connected,
and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house,
return the maximum amount of money you can rob tonight without alerting the police.

Example 1:
Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.

Example 2:
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 3:
Input: nums = [1,2,3]
Output: 3

Constraints:
1 <= nums.length <= 100
0 <= nums[i] <= 1000
'''
import array

class Solution:
    def rob(self, nums: list[int]) -> int:
        def robber(nums:list):
            number_of_houses = len(nums)
            OPT = array.array("i", [-1 for _ in range(number_of_houses)])
            OPT[0] = nums[0]
            OPT[1] = max(nums[0], nums[1])
            for i in range(2, number_of_houses):
                OPT[i] = max(nums[i] + OPT[i-2], OPT[i-1]) 
            return OPT[-1]
        len_of_nums = len(nums)
        if len_of_nums == 0:
            return 0
        if len_of_nums < 3:
            return max(nums)
        return max(robber(nums[:-1]), robber(nums[1:]))

print("nums = [2,3,2]:", Solution().rob(nums = [2,3,2])) # 3
print("nums = [1,2,3,1]:", Solution().rob(nums = [1,2,3,1])) # 4
print("nums = [1,2,3]:", Solution().rob(nums = [1,2,3])) # 3
print("nums = [2,3,1,1]:", Solution().rob(nums = [1,3,2,1])) # 4
print("nums = [1]:", Solution().rob(nums = [1])) # 1