'''
20. Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false
'''
class Solution:
	def isValid(self, s: str) -> bool:
		isValid = False
		stack = list()
		for character in s:
			if character in ['(', '{', '[']:
				stack.append(character)
			else:
				if stack:
					top_element = stack.pop()
					if character == ')' and top_element != '(':
						isValid = False
						break
					elif character == '}' and top_element != '{':
						isValid = False
						break
					elif character == ']' and top_element != '[':
						isValid = False
						break
					else:
						isValid = True
				else:
					isValid = False
					break
		if stack:
			isValid = False
		return isValid

print( "() :", Solution().isValid("()") )
print( "()[]{} :", Solution().isValid("()[]{}") )
print( "(] :", Solution().isValid("(]") )
print( "( :", Solution().isValid("(") )
print( "(( :", Solution().isValid("((") )
print( "(() :", Solution().isValid("(()") )
print( "] :", Solution().isValid("]") )
print( "([]){", Solution().isValid("([]){") )