class Solution:
    def minProductSum(self, nums1: List[int], nums2: List[int]) -> int:
        sum = 0
        for u,v in zip(sorted(nums1), sorted(nums2, reverse=True)):
            sum += (u*v)
        return sum