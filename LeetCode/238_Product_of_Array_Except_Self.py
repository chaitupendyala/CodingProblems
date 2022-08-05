'''
238. Product of Array Except Self
Medium

Given an integer array nums, return an array answer such that answer[i] 
is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 
Constraints:
2 <= nums.length <= 10^5
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
 

Follow up: Can you solve the problem in O(1) extra space complexity? 
(The output array does not count as extra space for space complexity analysis.)
'''
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        product = 0
        zero_exists, two_or_more_zero_exist = False, False
        for i in nums:
            if i != 0:
                if product == 0: product = 1
                product *= i
            else:
                if zero_exists:
                    two_or_more_zero_exist = True
                zero_exists = True
        output = []
        for i in range(len(nums)):
            if nums[i] != 0 and zero_exists:
                output.append(0)
                continue
            if nums[i] != 0 and not zero_exists:
                output.append(product // nums[i])
                continue
            
            if nums[i] == 0:
                if two_or_more_zero_exist:
                    output.append(0)
                else:
                    output.append(product)
        return output

print("nums = [1,2,3,4]:", Solution().productExceptSelf(nums = [1,2,3,4]))
print("nums = [-1,1,0,-3,3]:", Solution().productExceptSelf(nums = [-1,1,0,-3,3]))
print("nums = [0,4,0]:", Solution().productExceptSelf(nums = [0,4,0]))