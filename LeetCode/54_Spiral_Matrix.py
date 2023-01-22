class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        output = []
        no_of_rows, no_of_columns = len(matrix), len(matrix[0])
        left, up = 0, 0
        right, down = no_of_columns - 1, no_of_rows - 1
        while len(output) < no_of_rows * no_of_columns:
            for col in range(left, right+1):
                output.append(matrix[up][col])
            
            for row in range(up+1, down+1):
                output.append(matrix[row][right])
            
            if up != down:
                for col in range(right-1, left-1, -1):
                    output.append(matrix[down][col])
            
            if left != right:
                for row in range(down-1, up, -1):
                    output.append(matrix[row][left])
            
            up+=1
            down-=1
            left+=1
            right-=1
        return output