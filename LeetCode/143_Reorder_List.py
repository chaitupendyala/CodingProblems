'''
143. Reorder List
Medium

You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

Example 1:
Input: head = [1,2,3,4]
Output: [1,4,2,3]

Example 2:
Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]

Constraints:
The number of nodes in the list is in the range [1, 5 * 10^4].
1 <= Node.val <= 1000
'''
from operator import ne
from optparse import Option
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        '''
        We can solve it in 3 steps:
        1. Find the middle
        2. Reverse the second half of the list
        3. Merge the two halfs
        '''
        #Find the middle
        if not head:
            return
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        #Reverse the second half
        #This logic can also be used to reverse any linked list.
        previous, current = None, slow.next
        while current:
            next = current.next
            current.next = previous
            previous = current
            current = next
        slow.next = None

        #Merge the two lists
        head_list1, head_list2 = head, previous
        while head_list2:
            next = head_list1.next
            head_list1.next = head_list2
            head_list1 = head_list2
            head_list2 = next

#head = [1,2,3,4]
first = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
Solution().reorderList(first)
while first:
    print(first.val)
    first = first.next