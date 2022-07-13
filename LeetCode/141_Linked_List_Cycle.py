'''
141. Linked List Cycle
Easy

Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

Example 2:
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

Example 3:
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.

Constraints:
The number of the nodes in the list is in the range [0, 104].
-10^5 <= Node.val <= 10^5
pos is -1 or a valid index in the linked-list.
'''
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:    return False
        slow_pointer = head.next
        fast_pointer = head.next.next
        found_cycle = False
        while slow_pointer and fast_pointer:
            if slow_pointer == fast_pointer:
                found_cycle = True
                break
            else:
                if slow_pointer:
                    slow_pointer = slow_pointer.next
                else:
                    slow_pointer = None
                if fast_pointer.next:
                    fast_pointer = fast_pointer.next.next
                else:
                    fast_pointer = None
        return found_cycle


#head = [3,2,0,-4]
first = ListNode(3)
second = ListNode(2)
third = ListNode(0)
forth = ListNode(-4)
first.next = second
second.next = third
third.next = forth
forth.next = second
print("head = [3,2,0,-4]:", Solution().hasCycle(head= first))

#head = [1,2], pos = 0
first = ListNode(3)
second = ListNode(2)
first.next = second
second.next = first
print("head = [1,2]:", Solution().hasCycle(head= first))

#head = [1], pos = -1
first = ListNode(1)
print("head = [1]:", Solution().hasCycle(head= first))

#head = [], pos = -1
print("head = []:", Solution().hasCycle(head= None))