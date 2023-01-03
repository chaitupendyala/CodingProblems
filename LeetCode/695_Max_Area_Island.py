class Solution:
    max_area = 0
    visited = set()
    def dfs(self, grid, row, column):
            if row < 0 or column < 0 or row >= len(grid) or column >= len(grid[0]) or (row,column) in self.visited or grid[row][column] == 0:
                return 0
            self.visited.add((row,column))
            return 1 + self.dfs(grid, row+1, column) + self.dfs(grid, row-1, column) + self.dfs(grid, row, column+1) + self.dfs(grid, row, column-1)
    def maxAreaOfIsland(self, grid) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                current_area = self.dfs(grid, i, j)
                self.max_area = max(self.max_area, current_area)
        return self.max_area

print("grid = [[1,1,0,1,1],[1,0,0,0,0],[0,0,0,0,1],[1,1,0,1,1]]: ", Solution().maxAreaOfIsland(grid = [[1,1,0,1,1],[1,0,0,0,0],[0,0,0,0,1],[1,1,0,1,1]]))