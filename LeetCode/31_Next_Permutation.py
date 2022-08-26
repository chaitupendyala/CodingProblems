'''
31. Next Permutation
Medium

A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

For example, for arr = [1,2,3], the following are considered permutations of arr: [1,2,3], [1,3,2], [3,1,2], [2,3,1].
The next permutation of an array of integers is the next lexicographically greater permutation of its integer. 
More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, 
then the next permutation of that array is the permutation that follows it in the sorted container. 
If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

For example, the next permutation of arr = [1,2,3] is [1,3,2].
Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
Given an array of integers nums, find the next permutation of nums.

The replacement must be in place and use only constant extra memory.

Example 1:
Input: nums = [1,2,3]
Output: [1,3,2]

Example 2:
Input: nums = [3,2,1]
Output: [1,2,3]

Example 3:
Input: nums = [1,1,5]
Output: [1,5,1]

Constraints:
1 <= nums.length <= 100
0 <= nums[i] <= 100
'''
class Solution:
    '''
    Next lexicographical permutation algorithm(https://www.nayuki.io/page/next-lexicographical-permutation-algorithm):
    1. Find longest non-increasing suffix
    2. Identify Pivot - first element to the immediate left of the above sequence
    3. Find rightmost successor to the pivot in the sufix
    4. Swap the pivot and successor
    5. Reverse the sufix
    '''
    def nextPermutation(self, nums: list[int]) -> None:
        right = len(nums) - 1
        while ( nums[right] <= nums[right-1] and right >= 1  ):
            right -= 1
        
        if right == 0:
            nums[::] = nums[::-1]
            return
        
        pivot = right - 1
        successor = None
        for i in range(len(nums)-1, pivot, -1):
            if nums[i] > nums[pivot]:
                successor = i
                break
        nums[pivot], nums[successor] = nums[successor], nums[pivot]
        nums[pivot+1:len(nums):] = nums[len(nums) - 1:pivot:-1]

nums = [1,2,3]
Solution().nextPermutation(nums)
print("nums = [1,2,3]:", nums) #Output: [1,3,2]

nums = [3,2,1]
Solution().nextPermutation(nums)
print("nums = [3,2,1]:", nums) #Output: [1,2,3]

nums = [1,1,5]
Solution().nextPermutation(nums)
print("nums = [1,1,5]:", nums) #Output: [1,5,1]

nums = [1,3,2]
Solution().nextPermutation(nums)
print("nums = [1,3,2]:", nums) #Output: [2, 1, 3]

nums = [2,3,1]
#Solution().nextPermutation(nums)
print("nums = [2,3,1]:", nums) #Output: [3, 1, 2]