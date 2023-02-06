class Solution:
    def minPartitions(self, n: str) -> int:
        #We need atleast max(n) 1's to partition number into Deci-Binary numbers
        return int(max(n))