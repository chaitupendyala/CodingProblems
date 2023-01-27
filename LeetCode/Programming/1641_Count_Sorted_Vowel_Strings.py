'''
1641. Count Sorted Vowel Strings
Medium

Given an integer n, return the number of strings of length n that consist only of vowels (a, e, i, o, u) 
and are lexicographically sorted.

A string s is lexicographically sorted if for all valid i, s[i] is the same as or comes before s[i+1] in the alphabet.

Example 1:
Input: n = 1
Output: 5
Explanation: The 5 sorted strings that consist of vowels only are ["a","e","i","o","u"].

Example 2:
Input: n = 2
Output: 15
Explanation: The 15 sorted strings that consist of vowels only are
["aa","ae","ai","ao","au","ee","ei","eo","eu","ii","io","iu","oo","ou","uu"].
Note that "ea" is not a valid string since 'e' comes after 'a' in the alphabet.

Example 3:
Input: n = 33
Output: 66045

Constraints:
1 <= n <= 50 
'''
'''
OPT[i][j]: represents the number of strings of length i, starting with charecters of column j and after j

OPT[i][j] = OPT[i-1][j] + OPT[i][j+1]

So the solution would be OPT[n][0]
'''
class Solution:
    def countVowelStrings(self, n: int) -> int:
        OPT = [[i for i in range(5,0,-1)] for _ in range(n)]
        
        for i in range(1,n):
            for j in range(3,-1,-1):
                OPT[i][j] = OPT[i-1][j] + OPT[i][j+1]
        return OPT[n-1][0]

print("n = 1:",Solution().countVowelStrings(n = 1))
print("n = 2:",Solution().countVowelStrings(n = 2))
print("n = 33:",Solution().countVowelStrings(n = 33))