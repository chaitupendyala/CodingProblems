'''
206. Reverse Linked List
Easy

Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
Input: head = [1,2]
Output: [2,1]

Example 3:
Input: head = []
Output: []
'''
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        
        previous, current = None, head
        while current:
            next = current.next
            current.next = previous
            previous = current
            current = next
        return previous

head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
new_head = Solution().reverseList(head)
while new_head:
    print(new_head.val)
    new_head = new_head.next