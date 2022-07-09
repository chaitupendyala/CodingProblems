'''
102. Binary Tree Level Order Traversal - Medium

Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from
left to right, level by level).

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

Example 2:
Input: root = [1]
Output: [[1]]

Example 3:
Input: root = []
Output: []
'''
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

class Solution:
	def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
		level_order_traversal = list()
		level_order_queue = list()
		if root is None:
			return level_order_traversal
		level_order_queue.append([root])
		while True:
			next_level = list()
			current_level = list()
			for node in level_order_queue[0]:
				current_level.append(node.val)
				if node.left is not None:
					next_level.append(node.left)
				if node.right is not None:
					next_level.append(node.right)
			level_order_traversal.append(current_level)
			level_order_queue.pop(0)
			if len(next_level):
				level_order_queue.append(next_level)
			else:
				break
			current_level = list()
			next_level = list()
		return level_order_traversal

root = TreeNode( 3,
				 TreeNode( 9 ),
				 TreeNode( 20,
				 		   TreeNode(15),
				 		   TreeNode(7) ) )

print( "root = [3,9,20,null,null,15,7]: ", Solution().levelOrder(root) )

root = TreeNode(1)
print( "root = [1]: ", Solution().levelOrder(root) )

print( "root = []: ", Solution().levelOrder(None) )