'''
59. Spiral Matrix II
Medium

Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

Example 1:
Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]

Example 2:
Input: n = 1
Output: [[1]]

Constraints:
1 <= n <= 20
'''
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        left, top = 0, 0
        right, bottom = n-1, n-1
        counter = 0
        while counter < n ** 2:
            for i in range(left, right+1):
                counter+=1
                matrix[top][i] = counter
            
            for j in range(top+1, bottom+1):
                counter+=1
                matrix[j][right] = counter
            
            if top != bottom:
                for i in range(right-1, left-1, -1):
                    counter+=1
                    matrix[bottom][i] = counter
            if right != left:
                for j in range(bottom-1, top, -1):
                    counter+=1
                    matrix[j][left] = counter
            top+=1
            left+=1
            right-=1
            bottom-=1
        return matrix