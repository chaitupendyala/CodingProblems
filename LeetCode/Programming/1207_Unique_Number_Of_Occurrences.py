class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = collections.Counter(arr)
        return True if len(count.values()) == len(set(count.values())) else False