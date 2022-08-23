'''
417. Pacific Atlantic Water Flow
Medium

There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. 
The Pacific Ocean touches the island's left and top edges, 
and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. 
You are given an m x n integer matrix heights where heights[r][c] represents 
the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, 
and the rain water can flow to neighboring cells directly north, south, east, and west 
if the neighboring cell's height is less than or equal to the current cell's height. 
Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

Example 1:
Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]

Example 2:
Input: heights = [[2,1],[1,2]]
Output: [[0,0],[0,1],[1,0],[1,1]]
 

Constraints:

m == heights.length
n == heights[r].length
1 <= m, n <= 200
0 <= heights[r][c] <= 10^5
'''
class Solution:
    canReachPacific = []
    canReachAtlantic = []
    def dfs(self, heights, row, column, max_row, max_column) -> bool:
        if heights[row][column] == '#':
            return False
        if row <= 0 or column <= 0 or row >= max_row or column >= max_column:
            return True
        
        valid1, valid2, valid3, valid4 = False, False, False, False
        temp = heights[row][column]
        heights[row][column] = '#'
        if heights[row+1][column] != '#' and temp >= heights[row+1][column]:
            valid1 = self.dfs(heights, row + 1, column, max_row, max_column)
        if heights[row-1][column] != '#' and temp >= heights[row-1][column]:
            valid2 = self.dfs(heights, row - 1, column, max_row, max_column)
        if heights[row][column+1] != '#' and temp >= heights[row][column+1]:
            valid3 = self.dfs(heights, row, column + 1, max_row, max_column)
        if heights[row][column-1] != '#' and temp >= heights[row+1][column-1]:
            valid4 = self.dfs(heights, row, column - 1, max_row, max_column)
        heights[row][column] = temp
        return valid1 or valid2 or valid3 or valid4

    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        result = []
        num_of_rows = len(heights)
        num_of_columns = len(heights[0])
        self.canReachPacific = [ [None for _ in range(num_of_columns)] for _ in range)(num_of_rows) ]
        self.canReachPacific = [ [None for _ in range(num_of_columns)] for _ in range)(num_of_rows) ]
        #for i in range(num_of_rows):
        #    for j in range(num_of_columns):
        #        if self.dfs(heights, i, j, num_of_rows-1, num_of_columns-1):
        #            result.append([i,j])
        return result

print("heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]:",
      Solution().pacificAtlantic(heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]))
      #Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]

print("heights = [[2,1],[1,2]]:", Solution().pacificAtlantic(heights = [[2,1],[1,2]])) #Output:Output: [[0,0],[0,1],[1,0],[1,1]]