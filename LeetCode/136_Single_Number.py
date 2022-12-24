'''
136. Single Number
Easy

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1:
Input: nums = [2,2,1]
Output: 1

Example 2:
Input: nums = [4,1,2,1,2]
Output: 4

Example 3:
Input: nums = [1]
Output: 1
'''
'''
Approach: a XOR 0 = a
          a XOR a = 0
          a XOR b XOR a = (a XOR a) XOR b = b
          Therefore if we XOR all the numbers we will get the number that is occuring only once
'''
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        a = 0
        for i in nums:
            a ^= i
        return a