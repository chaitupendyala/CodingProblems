class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return nums[0]
        start = 0; end = len(nums)-1
        sum = 0
        while start<end:
            numbers = str(nums[start]) + str(nums[end])
            print(numbers)
            sum += int(numbers)
            start += 1
            end -= 1
        if len(nums) % 2 != 0:
            sum += int(nums[len(nums) // 2])
        return sum