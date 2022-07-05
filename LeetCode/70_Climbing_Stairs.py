'''
70. Climbing Stairs

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
'''
class Solution:
	MEM = list()
	def _climbStairs(self, n: int) -> int:
		if ( n == 0 ):
			return 0
		if ( n == 1 ):
			return 1
		if ( n == 2 ):
			return 2
		if ( self.MEM[n-1] != -1  ):
			return self.MEM[n-1]
		self.MEM[n-1] = self._climbStairs(n-1) + self._climbStairs(n-2)
		return self.MEM[n-1]
	def climbStairs(self, n: int) -> int:
		self.MEM = [-1 for _ in range(n)]
		return self._climbStairs(n)

print("n = 2: ", Solution().climbStairs(2))
print("n = 3: ", Solution().climbStairs(3))
print("n = 4: ", Solution().climbStairs(4))
print("n = 38: ", Solution().climbStairs(38))