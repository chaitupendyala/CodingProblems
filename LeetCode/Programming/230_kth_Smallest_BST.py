'''
230. Kth Smallest Element in a BST
Medium

Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

Example 1:
Input: root = [3,1,4,null,2], k = 1
Output: 1

Example 2:
Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3

Constraints:
The number of nodes in the tree is n.
1 <= k <= n <= 10^4
0 <= Node.val <= 10^4

Follow up: If the BST is modified often (i.e., we can do insert and delete operations) and you need 
           to find the kth smallest frequently, how would you optimize?
'''
#Obviously the simplest solution would be to do an inorder traversal and find the kth smallest.
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root, numbers):
        if not root:
            return
        self.inorderTraversal(root.left, numbers)
        numbers.append(root.val)
        self.inorderTraversal(root.right, numbers)
    def kthSmallest(self, root: Optional[TreeNode], k: int, nums = []) -> int:
        if not root:
            return
        numbers = []
        self.inorderTraversal(root, numbers)
        return numbers[k-1]

'''
             3
            / \
           /    \
          1      4
           \
            2
'''
root = TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4))
print("root = [3,1,4,null,2], k = 1:", Solution().kthSmallest(root, 1)) # Output: 1

'''
             5
            / \
           /    \
          3      6
         / \
        2   4
       /
      1
'''
root = TreeNode(5, TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(4)), TreeNode(6))
print("root = [5,3,6,2,4,null,null,1], k = 3:", Solution().kthSmallest(root, 3)) # Output: 3