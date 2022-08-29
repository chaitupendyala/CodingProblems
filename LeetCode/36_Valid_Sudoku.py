'''
36. Valid Sudoku
Medium

Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Note:
A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
 

Example 1:
Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true

Example 2:
Input: board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. 
Since there are two 8's in the top left 3x3 sub-box, it is invalid.
 

Constraints:

board.length == 9
board[i].length == 9
board[i][j] is a digit 1-9 or '.'.
'''
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #Are rows valid
        are_rows_valid = True
        for row in board:
            set_of_numbers = set()
            for number in row:
                if number == '.':
                    continue
                if int(number) not in set_of_numbers:
                    set_of_numbers.add(int(number))
                else:
                    are_rows_valid = False
                    break
        if not are_rows_valid:
            return False        
        
        #Are columns valid
        are_columns_valid = True
        for column in range(len(board[0])):
            set_of_numbers = set()
            for row in range(len(board)):
                if board[row][column] == '.':
                    continue
                if int(board[row][column]) not in set_of_numbers:
                    set_of_numbers.add(int(board[row][column]))
                else:
                    are_columns_valid = False
        if not are_columns_valid:
            return False
        
        #Are squares valid
        are_squares_valid = True
        for i in (0,3,6):
            for j in (0,3,6):
                square = [int(board[x][y]) for x in range(i,i+3) for y in range(j,j+3) if board[x][y] != '.']
                set_of_numbers = set()
                print(square)
                for number in square:
                    if number not in set_of_numbers:
                        set_of_numbers.add(number)
                    else:
                        are_squares_valid = False
                        break
        if not are_squares_valid:
            return False
        
        return True