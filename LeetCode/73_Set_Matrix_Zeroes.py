'''
73. Set Matrix Zeroes

Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
You must do it in place.

Example 1:
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

Example 2:
Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
'''
class Solution:
	def setZeroes(self, matrix: list[list[int]]) -> None:
		rows = set()
		columns = set()
		num_of_rows = len(matrix)
		num_of_columns = 0
		for i,row in enumerate(matrix):
			for j,n in enumerate(row):
				if (n == 0):
					rows.add(i)
					columns.add(j)
				num_of_columns = max(num_of_columns, j+1)

		for i in range(num_of_rows):
			if i in rows:
				matrix[i] = [0 for _ in range(num_of_columns)]
		for j in columns:
			for i in range(num_of_rows):
				matrix[i][j] = 0


print("matrix = [[1,1,1],[1,0,1],[1,1,1]]: ", Solution().setZeroes([[1,1,1],[1,0,1],[1,1,1]]))
print("matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]: ", Solution().setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]]))