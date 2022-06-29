'''
22. Generate Parentheses
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
'''
class Solution:
	def generate( self, p, left, right, parentheses=[] ):
		if left:
			self.generate( p + '(', left - 1, right     )
		if right > left:
			self.generate( p + ')', left    , right - 1 )
		if not right:
			parentheses.append(p)
		return parentheses
	def generateParenthesis(self, n: int) -> list[str]:
		return self.generate( '', n, n )

print(Solution().generateParenthesis(3))