'''
139. Word Break
Medium

Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a
space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

Example 1:
Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Example 2:
Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.

Example 3:
Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false

Constraints:
1 <= s.length <= 300
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 20
s and wordDict[i] consist of only lowercase English letters.
All the strings of wordDict are unique.
'''
class Solution:
	def wordBreak(self, s: str, wordDict: list[str]) -> bool:
		length_of_string = len(s)
		OPT = [False for _ in range(length_of_string)]
		for i in range(length_of_string):
			for word in wordDict:
				length_of_word = len(word)
				if ( word == s[i - length_of_word + 1:i+1] and (OPT[i-length_of_word] or i-length_of_word == -1) ):
					OPT[i] = True
		return OPT[-1]

print('s = "leetcode", wordDict = ["leet","code"]:', Solution().wordBreak(s = "leetcode", wordDict = ["leet","code"]))
print('s = "laetcode", wordDict = ["leet","code"]:', Solution().wordBreak(s = "laetcode", wordDict = ["leet","code"]))
print('s = "applepenapple", wordDict = ["apple","pen"]:', Solution().wordBreak(s = "applepenapple", wordDict = ["apple","pen"]))
print('s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]:', Solution().wordBreak(s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]))
print('s = "aaaaaaa", wordDict = ["aaaa","aaa"]:', Solution().wordBreak(s = "aaaaaaa", wordDict = ["aaaa","aaa"]))