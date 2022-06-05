'''
Longest Palindromic Substring

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Input: s = "cbbd"
Output: "bb"
'''

class Solution:
	def longestPalindrome(self, s: str) -> str:
		OPT = [[0 for _ in range(len(s))] for _ in range(len(s))]
		i = 0
		j = len(s)
		return OPT

s = Solution()
print("ABC:", s.longestPalindrome("ABC"))