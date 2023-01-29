"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        
        #Goto the leftmost node first
        leftmost = root
        while leftmost.left:
            head = leftmost
            while head:
                #The left node's next node will be the right node
                head.left.next = head.right
                if head.next:
                    #The right node's next will be parent's next's left node
                    head.right.next = head.next.left
                #Move to the next node
                head = head.next
            
            leftmost = leftmost.left
        return root