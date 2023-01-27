'''
200. Number of Islands
Medium

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), 
return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water.

Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
'''
from numpy import number
from pyparsing import col


class Solution:
    def dfs(self, grid, row, column, number_of_rows, number_of_columns):
        if row < 0 or column < 0 or row >= number_of_rows or column >= number_of_columns or grid[row][column] != '1':
            return
        grid[row][column] = None
        self.dfs(grid, row+1,column, number_of_rows, number_of_columns)
        self.dfs(grid, row-1,column, number_of_rows, number_of_columns)
        self.dfs(grid, row,column+1, number_of_rows, number_of_columns)
        self.dfs(grid, row,column-1, number_of_rows, number_of_columns)

    def numIslands(self, grid: list[list[str]]) -> int:
        number_of_islands = 0
        number_of_rows = len(grid)
        number_of_columns = len(grid[0])
        for row in range(number_of_rows):
            for column in range(number_of_columns):
                if grid[row][column] == '1':
                    self.dfs(grid, row, column, number_of_rows, number_of_columns)
                    number_of_islands += 1
        return number_of_islands

print('grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]:', Solution().numIslands(grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]))

print('grid = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]:', Solution().numIslands(grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]))