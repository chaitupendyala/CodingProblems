'''
347. Top K Frequent Elements
Medium

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]

Constraints:
1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
'''
from collections import Counter

# class Solution:
#     def topKFrequent(self, nums: list[int], k: int) -> list[int]:
#         frequency = Counter(nums).most_common(k)
#         return [i[0] for i in frequency]
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        frequency = Counter(nums)
        reverse_frequency = {}
        for key, value in frequency.items():
            if value not in reverse_frequency:
                reverse_frequency[value] = [key]
            else:
                reverse_frequency[value].append(key)
        result = []
        for i in range(len(nums), 0, -1):
            if i in reverse_frequency:
                for j in reverse_frequency[i]:
                    result.append(j)
        
        return result[:k]

print("nums = [1,1,1,2,2,3], k = 2:", Solution().topKFrequent(nums = [1,1,1,2,2,3], k = 2))
print("nums = [1], k = 1:", Solution().topKFrequent(nums = [1], k = 1))
print("nums = [3,0,1,0], k = 1:", Solution().topKFrequent(nums = [3,0,1,0], k = 1))