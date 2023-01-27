'''
212. Word Search II
Hard
Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, 
where adjacent cells are horizontally or vertically neighboring. 
The same letter cell may not be used more than once in a word.

Example 1:
Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]

Example 2:
Input: board = [["a","b"],["c","d"]], words = ["abcb"]
Output: []
'''
from collections import defaultdict
class TrieNode:
    def __init__(self, char) -> None:
        self.children = defaultdict(TrieNode)
        self.is_word = False
        self.char = char

class Trie:
    def __init__(self):
        self.root = TrieNode('*')
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                new_node = TrieNode(char)
                node.children[char] = new_node
                node = new_node
        node.is_word = True

class Solution:
    def valid_word(self, board, node, i, j, path, result):
        if node.is_word:
            result.append(path)
            node.is_word = False
        
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return
        
        temp = board[i][j]
        node = node.children.get(temp)
        if not node:
            return False
        board[i][j] = "$"
        self.valid_word(board, node, i+1, j, path+temp, result)
        self.valid_word(board, node, i-1, j, path+temp, result)
        self.valid_word(board, node, i, j+1, path+temp, result)
        self.valid_word(board, node, i, j-1, path+temp, result)
        board[i][j] = temp

    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        result = list()
        trie = Trie()
        node = trie.root
        for w in words:
            trie.insert(w)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.valid_word(board, node, i, j, "", result)

        return result

#Output: ["eat","oath"]
print('board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]:',
      Solution().findWords(board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]))

#Output: []
print('board = [["a","b"],["c","d"]], words = ["abcb"]:',
      Solution().findWords(board = [["a","b"],["c","d"]], words = ["abcb"]))