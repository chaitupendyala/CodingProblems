from collections import defaultdict
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        count = 0
        mod  = defaultdict(int)
        for i in range(len(time)):
            if time[i] % 60 == 0:
                count += mod[0]
            else:
                count += mod[60-(time[i]%60)]
            mod[time[i]%60] += 1
        return count