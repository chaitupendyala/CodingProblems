'''
242. Valid Anagram
Easy

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once. 

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

Constraints:
1 <= s.length, t.length <= 5 * 10^4
s and t consist of lowercase English letters.
 

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        alphabet_occurances = dict()
        for i in range(len(s)):
            if s[i] not in alphabet_occurances:
                values = [1,0]
                alphabet_occurances[s[i]] = values
            else:
                alphabet_occurances[s[i]][0] += 1
            if t[i] not in alphabet_occurances:
                values = [0,1]
                alphabet_occurances[t[i]] = values
            else:
                alphabet_occurances[t[i]][1] += 1
        for key in alphabet_occurances.keys():
            if alphabet_occurances[key][0] != alphabet_occurances[key][1]:
                return False
        
        return True

print('s = "anagram", t = "nagaram":', Solution().isAnagram(s = "anagram", t = "nagaram"))
print('s = "rat", t = "car":', Solution().isAnagram(s = "rat", t = "car"))