'''
3. Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''
class Solution:
	def lengthOfLongestSubstring(self, s: str) -> int:
		encountered_charecters = {}
		longest_substring = 0
		start_index = 0
		for index in range(len(s)):
			if s[index] in encountered_charecters and start_index <= encountered_charecters[s[index]]:
				start_index = encountered_charecters[s[index]] + 1
			else:
				longest_substring = max( longest_substring, index - start_index + 1 )
			encountered_charecters[s[index]] = index

		return longest_substring

print( "abcabcbb: ", Solution().lengthOfLongestSubstring('abcabcbb') )
print( "bbbbb: ", Solution().lengthOfLongestSubstring('bbbbb') )
print( "pwwkew: ", Solution().lengthOfLongestSubstring('pwwkew') )
print( "aab: ", Solution().lengthOfLongestSubstring('aab') )
print( "dvdf: ", Solution().lengthOfLongestSubstring("dvdf") )