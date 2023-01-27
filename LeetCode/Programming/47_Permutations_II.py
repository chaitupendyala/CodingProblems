'''
47. Permutations II
Medium

Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order. 

Example 1:
Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]

Example 2:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Constraints:
1 <= nums.length <= 8
-10 <= nums[i] <= 10
'''
class Solution:
    def dfs(self, decision_space, path, result):
        if not decision_space:
            result.add(tuple(path))
            return
        for i in range(len(decision_space)):
            self.dfs(decision_space[:i] + decision_space[i+1:], path + [decision_space[i]], result)
    
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        result = set()
        self.dfs(nums, [], result)
        result = list(map(list, result))
        return result


print("nums = [1,1,2]:", Solution().permuteUnique(nums = [1,1,2]))
print("nums = [1,2,3]:", Solution().permuteUnique(nums = [1,2,3]))