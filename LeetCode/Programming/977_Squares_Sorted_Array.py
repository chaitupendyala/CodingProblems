'''
977. Squares of a Sorted Array
Easy

Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

Example 1:
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].

Example 2:
Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
'''
class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        left, right = 0, len(nums) - 1
        result = [0] * (right + 1)
        for i in range(right, -1, -1):
            number_to_square = 0
            if abs(nums[left]) < abs(nums[right]):
                number_to_square = nums[right]
                right -= 1
            else:
                number_to_square = nums[left]
                left += 1
            result[i] = number_to_square ** 2
        return result