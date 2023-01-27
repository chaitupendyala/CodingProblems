'''
76. Minimum Window Substring

Given two strings s and t of lengths m and n respectively, return the minimum window substring of s
such that every character in t (including duplicates) is included in the window. If there is no
such substring, return the empty string "".
The testcases will be generated such that the answer is
unique. 
A substring is a contiguous sequence of characters within the string.

Example 1:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Example 2:
Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.

Example 3:
Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.

Follow up: Could you find an algorithm that runs in O(m + n) time?
'''
class Solution:
	def minWindow(self, s: str, t: str) -> str:
		if len(t) > len(s):
			return ""
		letter_occurances = dict()
		for index, charecter in enumerate(s):
			if ( charecter not in letter_occurances ):
				letter_occurances[charecter] = set()
			letter_occurances[charecter].add(index)
		start, end = len(s), 0
		max_list = list()
		for char in t:
			if char not in letter_occurances:
				return ""
			occurances = list(letter_occurances[char])
			max_index = max(occurances)
			max_list.append(max_index)
			letter_occurances[char].remove(max_index)
		return s[min(max_list):max(max_list)+1]

print("s = \"ADOBECODEBANC\", t = \"ABC\": ", Solution().minWindow("ADOBECODEBANC", "ABC"))
print("s = \"a\", t = \"a\": ", Solution().minWindow("a", "a"))
print("s = \"a\", t = \"aa\": ", Solution().minWindow("a", "aa"))
print("s = \"aa\", t = \"aa\": ", Solution().minWindow("aa", "aa"))
print("s = \"cabwefgewcwaefgcf\", t = \"cae\": ", Solution().minWindow("cabwefgewcwaefgcf", "cae"))
'''
Input
"cabwefgewcwaefgcf"
"cae"

Output
"aefgc"

Expected
"cwae"
'''