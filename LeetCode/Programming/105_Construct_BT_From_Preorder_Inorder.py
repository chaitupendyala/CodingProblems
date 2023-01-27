'''
105. Construct Binary Tree from Preorder and Inorder Traversal
Medium

Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary
tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

Example 1:
Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]

Example 2:
Input: preorder = [-1], inorder = [-1]
Output: [-1]

Constraints:
============
- 1 <= preorder.length <= 3000
- inorder.length == preorder.length
- -3000 <= preorder[i], inorder[i] <= 3000
- preorder and inorder consist of unique values.
- Each value of inorder also appears in preorder.
- preorder is guaranteed to be the preorder traversal of the tree.
- inorder is guaranteed to be the inorder traversal of the tree.
'''
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

class Solution:
	def buildTree(self, preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
		number_of_nodes = len(preorder)
		root = None

		set_inorder = set()
		stack_preorder = list()

		preorder_index = 0
		inorder_index = 0

		while ( preorder_index < number_of_nodes ):
			while True:
				node = TreeNode(preorder[preorder_index])

				if not root:
					root = node

				if ( len(stack_preorder) != 0 ):
					if ( stack_preorder[-1] in set_inorder ):
						stack_preorder[-1].left = node
						stack_preorder.remove(stack_preorder.pop())
					else:
						stack_preorder[-1].left = node

				stack_preorder.append(node)

				preorder_index += 1
				if ( preorder_index >= number_of_nodes or preorder[preorder_index] == inorder[inorder_index] ):
					break

			node = None

			while ( len(stack_preorder) > 0 and inorder_index < number_of_nodes and stack_preorder[-1].val == inorder[inorder_index] ):
				node = stack_preorder.pop()
				inorder_index += 1

			if ( node != None ):
				set_inorder.add(node)
				stack_preorder.append(node)

		return root


print( "preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]: ", Solution().buildTree([3,9,20,15,7], [9,3,15,20,7]) )