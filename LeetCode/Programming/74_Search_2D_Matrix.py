from bisect import bisect_left
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binarySearch(row, target):
            i = bisect_left(row, target)
            if i != len(row) and row[i] == target:
                return True
            return False
        
        minRow, maxRow = 0, len(matrix)-1
        while minRow<=maxRow:
            midRow = (minRow + maxRow) // 2
            if matrix[midRow][0] <= target and matrix[midRow][-1] >= target:
                return binarySearch(matrix[midRow], target)
            elif matrix[midRow][-1] < target:
                minRow = midRow + 1
            else:
                maxRow = midRow - 1
        return False