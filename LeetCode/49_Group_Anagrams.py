'''
49. Group Anagrams

Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]
'''
class Solution:
	def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
		dict_of_similar_words = dict()
		for word in strs:
			sorted_string = ''.join(sorted(word))
			if sorted_string not in dict_of_similar_words:
				dict_of_similar_words[sorted_string] = [word]
			else:
				dict_of_similar_words[sorted_string].append(word)
		return list(dict_of_similar_words.values())

print('["eat","tea","tan","ate","nat","bat"]: ', Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"]))