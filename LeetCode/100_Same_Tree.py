'''
100. Same Tree

Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the
same value.

Example 1:
Input: p = [1,2,3], q = [1,2,3]
Output: true

Example 2:
Input: p = [1,2], q = [1,null,2]
Output: false

Example 3:
Input: p = [1,2,1], q = [1,1,2]
Output: false
'''
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

class Solution:
	def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
		if not p and not q:
			return True
		if (p and not q) or (not p and q) or (p.val != q.val):
			return False
		else:
			return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

p = TreeNode(1, TreeNode(2), TreeNode(3))
q = TreeNode(1, TreeNode(2), TreeNode(3))
print("p = [1,2,3], q = [1,2,3]: ", Solution().isSameTree(p,q))

p = TreeNode(1, TreeNode(2))
q = TreeNode(1, None, TreeNode(2))
print("p = [1,2], q = [1,null,2]: ", Solution().isSameTree(p,q))

p = TreeNode(1, TreeNode(2), TreeNode(1))
q = TreeNode(1, TreeNode(1), TreeNode(2))
print("p = [1,2,1], q = [1,1,2]: ", Solution().isSameTree(p,q))