'''
5. Longest Palindromic Substring

Given a string s, return the longest palindromic substring in s.

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
'''
class Solution:
	def longestPalindrome(self, s: str) -> str:
		length_of_string = len(s)
		max_length = 0
		start = 0

		for index in range(length_of_string):
			low = high = index
			if ( length_of_string % 2 == 0 ):
				high = index + 1

			while ( high < length_of_string and low >= 0 and s[high] == s[low] ):
				low -= 1
				high += 1

			if ( max_length < (high - low - 1) ):
				max_length = high - low - 1
				start = low + 1
		return s[start:start + max_length]


print("babad: " + Solution().longestPalindrome("babad"))
print("cbbd: " + Solution().longestPalindrome("cbbd"))
print("aba: " + Solution().longestPalindrome("aba"))