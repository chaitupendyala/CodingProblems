class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        number_of_possible_pairs = 0
        for i in range(len(nums)):
            left_index = bisect.bisect_left(nums, lower-nums[i], i+1, len(nums))
            right_index = bisect.bisect_right(nums, upper-nums[i], i+1, len(nums))
            number_of_possible_pairs += (right_index - left_index)
        return number_of_possible_pairs