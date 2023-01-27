'''
567. Permutation in String
Medium

Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

Example 1:
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:
Input: s1 = "ab", s2 = "eidboaoo"
Output: false
'''
from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if not s1 or not s2:
            return False
        len_of_s1 = len(s1)
        len_of_s2 = len(s2)
        if len_of_s1 > len_of_s2:
            return False
        s1_counter = Counter(s1)
        for i in range(0, len_of_s2 - len_of_s1 + 1):
            s2_counter = Counter(s2[i:i+len_of_s1])
            if s1_counter == s2_counter:
                return True
        return False