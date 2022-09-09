'''
1277. Count Square Submatrices with All Ones
Medium

Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.

Example 1:
Input: matrix =
[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
Output: 15
Explanation: 
There are 10 squares of side 1.
There are 4 squares of side 2.
There is  1 square of side 3.
Total number of squares = 10 + 4 + 1 = 15.

Example 2:
Input: matrix = 
[
  [1,0,1],
  [1,1,0],
  [1,1,0]
]
Output: 7
Explanation: 
There are 6 squares of side 1.  
There is 1 square of side 2. 
Total number of squares = 6 + 1 = 7.

Constraints:
1 <= arr.length <= 300
1 <= arr[0].length <= 300
0 <= arr[i][j] <= 1
'''
'''
dp[i][j] represent edge length of the biggest square whose lower right corner element is matrix[i][j]. Also there are dp[i][j] squares whose lower right corner element are matrix[i][j]. The answer of count-square-submatrices-with-all-ones is sum of all dp[i][j].

As Figure, the square edge length ( whose lower right corner element is matrix[i][j] ) is not greater than the minimum of three arrows + 1.

Fortunately it can be equal to when matrix[i][j]==1. On this condition dp[i][j]=the minimum of three arrows + 1;

And when matrix[i][j]==0 , dp[i][j]=0.

So

if matrix[i][j]==1 : 
    if i!=0 and j!=0: 
        dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])+1
    else: 
        dp[i][j] = 0 + 1
else:
    dp[i][j] = 0
'''
from unittest import result


class Solution:
  def countSquares(self, matrix: list[list[int]]) -> int:
    m, n = len(matrix), len(matrix[0])
    OPT = [[0] * (n+1) for _ in range(m+1)]
    result = 0
    for i in range(m):
      for j in range(n):
        if matrix[i][j] == 1:
          OPT[i+1][j+1] = min(OPT[i+1][j], OPT[i][j+1], OPT[i][j])+1
          result += OPT[i+1][j+1]
    return result

print("matrix =[[0,1,1,1],[1,1,1,1],[0,1,1,1]]:", Solution().countSquares(matrix =
[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]))

print("matrix = [[1,0,1],[1,1,0],[1,1,0]]:", Solution().countSquares(matrix = 
[
  [1,0,1],
  [1,1,0],
  [1,1,0]
]))