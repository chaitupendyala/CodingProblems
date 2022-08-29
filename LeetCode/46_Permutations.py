'''
46. Permutations
Medium

Given an array nums of distinct integers, return all the possible permutations. 
You can return the answer in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:
Input: nums = [0,1]
Output: [[0,1],[1,0]]

Example 3:
Input: nums = [1]
Output: [[1]]

Constraints:
1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.
'''
# import itertools
# map(list, itertools.permutations(nums))
# The above can be done to return all the permutations
class Solution:
    def dfs(self, decision_space, path, result):
        if not decision_space:
            result.append(path)
            return
        for i in range(len(decision_space)):
            self.dfs(decision_space[:i] + decision_space[i+1:], path + [decision_space[i]], result)
    
    def permute(self, nums: list[int]) -> list[list[int]]:
        result = []
        self.dfs(nums, [], result)
        return result


print("nums = [1,2,3]:", Solution().permute(nums = [1,2,3]))
print("nums = [0,1]:", Solution().permute(nums = [0,1]))
print("nums = [1]:", Solution().permute(nums = [1]))