'''
189. Rotate Array
Medium

Given an array, rotate the array to the right by k steps, where k is non-negative.

Example 1:
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

Example 2:
Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
'''
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        len_of_nums = len(nums)
        k = k % len_of_nums
        for i in range(abs(len_of_nums-k)//2):
            nums[i], nums[len_of_nums-k-i-1] = nums[len_of_nums-k-i-1], nums[i]
        for j in range(k//2):
            nums[len_of_nums-k+j], nums[-j-1] = nums[-j-1], nums[len_of_nums-k+j]
        nums.reverse()