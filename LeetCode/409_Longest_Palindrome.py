from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = Counter(s)
        max_len = 0
        for count in counter.values():
            max_len += count // 2 * 2
            if max_len % 2 == 0 and count % 2 == 1:
                max_len += 1
        return max_len