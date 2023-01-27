'''
19. Remove Nth Node From End of List

Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 1
Output: [1]

Follow up: Could you do this in one pass?
'''

# Definition for singly-linked list.
from typing import Optional

class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

class Solution:
	def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
		fast = slow = head

		for _ in range(n):
			fast = fast.next

		if not fast:
			return head.next

		while ( fast.next is not None ):
			fast = fast.next
			slow = slow.next

		slow.next = slow.next.next
		return head

node_1 = ListNode(1)
node_2 = ListNode(2)
node_3 = ListNode(3)
node_4 = ListNode(4)
node_5 = ListNode(5)

node_1.next = node_2
node_2.next = node_3
node_3.next = node_4
node_4.next = node_5

ret = Solution().removeNthFromEnd(node_1, 2)
node = ret
while( node is not None ):
	print(node.val)
	node = node.next