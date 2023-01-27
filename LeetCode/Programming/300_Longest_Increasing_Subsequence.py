'''
300. Longest Increasing Subsequence
Medium

Given an integer array nums, return the length of the longest strictly increasing subsequence.

A subsequence is a sequence that can be derived from an array by deleting some or no elements
without changing the order of the remaining elements. For example, [3,6,2,7] is a subsequence 
of the array [0,3,1,6,2,2,7].

Example 1:
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

Example 2:
Input: nums = [0,1,0,3,2,3]
Output: 4

Example 3:
Input: nums = [7,7,7,7,7,7,7]
Output: 1

Constraints:
1 <= nums.length <= 2500
-104 <= nums[i] <= 104

Follow up: Can you come up with an algorithm that runs in O(n log(n)) time complexity?
'''
class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        length_of_nums = len(nums)
        OPT = [1] * length_of_nums
        for i in range(1, length_of_nums):
            for j in range(i):
                if nums[i] > nums[j]:
                    OPT[i] = max(OPT[i], 1 + OPT[j])
        return max(OPT)
# Time Complexity: O(n^2)
# Space Complexity: O(n)

print("nums = [10,9,2,5,3,7,101,18]:", Solution().lengthOfLIS(nums = [10,9,2,5,3,7,101,18])) #Output: 4
print("nums = [0,1,0,3,2,3]:", Solution().lengthOfLIS(nums = [0,1,0,3,2,3])) #Output: 4
print("nums = [7,7,7,7,7,7,7]:", Solution().lengthOfLIS(nums = [7,7,7,7,7,7,7])) #Output: 1