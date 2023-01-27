class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return
        visited = set()
        i, j = 0, 0
        while j < len(nums):
            if nums[j] not in visited:
                nums[i] = nums[j]
                i+=1
                visited.add(nums[j])
            j+=1
        return nums[:i]

print("[1,1,2]: ", Solution().removeDuplicates([1,1,2]))
print("[0,0,1,1,1,2,2,3,3,4]: ", Solution().removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
print("[0,0,0,1,2,3,3,4]: ", Solution().removeDuplicates([0,0,0,1,2,3,3,4]))
print("[0,1,2,3,4]: ", Solution().removeDuplicates([0,1,2,3,4]))
print("[]: ", Solution().removeDuplicates([]))
print("None: ", Solution().removeDuplicates(None))