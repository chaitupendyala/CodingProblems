'''
21. Merge Two Sorted Lists

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]
'''
from typing import Optional

# Definition for singly-linked list.
class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

class Solution:
	def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
		combined_list = head_pointer = ListNode()
		while ( list1 != None or list2 != None ):
			if list1 == None and list2 != None:
				combined_list.next = list2
				list2 = list2.next
			elif list1 != None and list2 == None:
				combined_list.next = list1
				list1 = list1.next
			elif list1.val >= list2.val:
				combined_list.next = list2
				list2 = list2.next
			else:
				combined_list.next = list1
				list1 = list1.next
			combined_list = combined_list.next
		return head_pointer.next


list1_val1 = ListNode(1)
list1_val2 = ListNode(2)
list1_val3 = ListNode(4)
list1_val1.next = list1_val2
list1_val2.next = list1_val3

list2_val1 = ListNode(1)
list2_val2 = ListNode(3)
list2_val3 = ListNode(4)
list2_val1.next = list2_val2
list2_val2.next = list2_val3

combined_list = Solution().mergeTwoLists(list1_val1, list2_val1)

while( combined_list is not None ):
	print(combined_list.val)
	combined_list = combined_list.next