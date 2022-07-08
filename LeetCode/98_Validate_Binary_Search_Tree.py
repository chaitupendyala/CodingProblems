'''
98. Validate Binary Search Tree

Given the root of a binary tree, determine if it is a valid binary search tree (BST).
A valid BST is defined as follows:
The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

Example 1:
Input: root = [2,1,3]
Output: true

Example 2:
Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
'''
# Definition for a binary tree node.
from typing import Optional
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

class Solution:
	'''
	There are two ways to solve this:
	1. Run a inorder traversal and check if it is sorted.
	2. Keep passing the lowest and largest value and check if the root value is lower or greater than that.
	   This will save the extra O(n) traversal we need to perform at he end of the previous method.
	'''
	def isValidBST(self, root: Optional[TreeNode], lessThan = float('inf'), largerThan = float('-inf')):
		if not root:
			return True
		if root.val <= largerThan or root.val >= lessThan:
			return False
		return self.isValidBST(root.left, min(lessThan, root.val), largerThan) and \
			   self.isValidBST(root.right, lessThan, max(largerThan, root.val))

'''d = TreeNode(3)
e = TreeNode(6)
b = TreeNode(1)
c = TreeNode(4,d,e)
a = TreeNode(5,b,c)

print("root = [0,-1]: ", Solution().isValidBST(a))
'''
'''a = TreeNode(2)
b = TreeNode(2)
c = TreeNode(2,a,b)
print("root = [2,2,2]: ", Solution().isValidBST(c))'''
d = TreeNode(3)
e = TreeNode(7)
b = TreeNode(4)
c = TreeNode(6,d,e)
a = TreeNode(5,b,c)

print("root = [5,4,6,null,null,3,7]: ", Solution().isValidBST(a))