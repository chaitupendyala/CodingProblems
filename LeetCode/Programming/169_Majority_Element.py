'''
169. Majority Element
Easy

Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Example 1:
Input: nums = [3,2,3]
Output: 3

Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2 

Follow-up: Could you solve the problem in linear time and in O(1) space?
'''
'''
Boyer-Moore Voting Algorithm

Essentially, what Boyer-Moore does is look for a suffix sufsufsuf of nums where 
suf[0] is the majority element in that suffix. To do this, we maintain a count, 
which is incremented whenever we see an instance of our current candidate for majority 
element and decremented whenever we see anything else. Whenever count equals 0, 
we effectively forget about everything in nums up to the current index and consider 
the current number as the candidate for majority element. It is not immediately obvious 
why we can get away with forgetting prefixes of nums - consider the following examples 
(pipes are inserted to separate runs of nonzero count).
'''
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        count = 0
        candidate = None
        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1
        return candidate