'''
217. Contains Duplicate
Easy

Given an integer array nums, return true if any value appears at least twice in the array, 
and return false if every element is distinct. 

Example 1:
Input: nums = [1,2,3,1]
Output: true

Example 2:
Input: nums = [1,2,3,4]
Output: false

Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true

Constraints:
1 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
'''
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        nums_set = set()
        for num in nums:
            if num in nums_set:
                return True
            nums_set.add(num)
        return False

print("nums = [1,2,3,1]:",Solution().containsDuplicate(nums = [1,2,3,1]))
print("nums = [1,2,3,4]:",Solution().containsDuplicate(nums = [1,2,3,4]))
print("nums = [1,1,1,3,3,4,3,2,4,2]:",Solution().containsDuplicate(nums = [1,1,1,3,3,4,3,2,4,2]))