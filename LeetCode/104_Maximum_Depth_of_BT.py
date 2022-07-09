'''
104. Maximum Depth of Binary Tree

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down
to the farthest leaf node.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:
Input: root = [1,null,2]
Output: 2
'''
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

class Solution:
	def maxDepth(self, root: Optional[TreeNode]) -> int:
		if root is None:
			return 0
		return max( self.maxDepth(root.left), self.maxDepth(root.right) ) + 1

root = TreeNode( 3,
				 TreeNode( 9 ),
				 TreeNode( 20,
				 		   TreeNode(15),
				 		   TreeNode(7) ) )

print( "root = [3,9,20,null,null,15,7]: ", Solution().maxDepth(root) )

root = TreeNode( 1, 
				 None,
				 TreeNode(2) )
print( "root = [1,null,2]: ", Solution().maxDepth(root) )