'''
79. Word Search

Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are
horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example 1:
Input: board = [["A","B","C","E"],
				["S","F","C","S"],
				["A","D","E","E"]], word = "ABCCED"
Output: true

Example 2:
Input: board = [["A","B","C","E"],
				["S","F","C","S"],
				["A","D","E","E"]], word = "SEE"
Output: true

Example 3:
Input: board = [["A","B","C","E"],
				["S","F","C","S"],
				["A","D","E","E"]], word = "ABCB"
Output: false
'''
class Solution:
	def _exist(self, board: list[list[str]], word: str, row: int, column: int, number_of_rows: int, number_of_columns: int) -> bool:
		if ( word == "" ):
			return True

		if ( row < 0 or row > number_of_rows - 1 ):
			return False

		if ( column < 0 or column > number_of_columns - 1 ):
			return False

		if board[row][column] == '$':
			return False

		if ( board[row][column] != word[0] ):
			return False

		temp = board[row][column]
		board[row][column] = '$'
		found = self._exist( board, word[1:], row + 1, column, number_of_rows, number_of_columns ) or self._exist( board, word[1:], row - 1, column, number_of_rows, number_of_columns ) or self._exist( board, word[1:], row, column + 1, number_of_rows, number_of_columns ) or self._exist( board, word[1:], row, column - 1, number_of_rows, number_of_columns )
		if not found:
			board[row][column] = temp
		return found


	def exist(self, board: list[list[str]], word: str) -> bool:
		if len(board) == 0:
			return False
		number_of_rows = len(board)
		number_of_columns = len(board[0])
		for i in range(number_of_rows):
			for j in range(number_of_columns):
				if self._exist(board, word, i, j, number_of_rows, number_of_columns):
					return True
		return False
		

print('board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED": ', Solution().exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"))
print('board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE": ', Solution().exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE"))
print('board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB": ', Solution().exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB"))
print('board = [["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","B"],["A","A","A","A","B","A"]], word = "AAAAAAAAAAAAABB": ', Solution().exist([["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","B"],["A","A","A","A","B","A"]], "AAAAAAAAAAAAABB"))
print('board = [["C","A","A"],["A","A","A"],["B","C","D"]], word = "AAB": ', Solution().exist([["C","A","A"],["A","A","A"],["B","C","D"]], "AAB"))