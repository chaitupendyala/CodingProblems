'''
28. Find the Index of the First Occurrence in a String
Medium

Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.

Example 2:
Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
'''
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        length_of_needle = len(needle)
        length_of_haystack = len(haystack)
        if length_of_needle > length_of_haystack:
            return -1
        k = 0
        for i,v in enumerate(haystack):
            if v == needle[0]:
                j = 0
                while(j <= length_of_needle - 1 and i+j <= length_of_haystack - 1 and needle[j] == haystack[i+j]):
                    j+=1
                if j == length_of_needle:
                    return i
        return -1