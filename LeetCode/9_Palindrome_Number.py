'''
9. Palindrome Number

Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.

For example, 121 is a palindrome while 123 is not.
 

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
'''

class Solution:
	def isPalindrome(self, x: int) -> bool:
		str_int = str(x)
		len_str_int = len(str_int)
		middle_index = 0
		if ( len(str_int) % 2 == 0 ):
			middle_index = len_str_int/2
		else:
			middle_index = (len_str_int + 1)/2

		start = 0
		end = len_str_int - 1
		palindrome = True
		while (start != middle_index):
			if str_int[start] != str_int[end]:
				palindrome = False
				break
			start += 1
			end -= 1
		return palindrome

print( "121: ", Solution().isPalindrome(121) )
print( "-121: ", Solution().isPalindrome(-121) )
print( "10: ", Solution().isPalindrome(10) )