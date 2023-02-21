# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sentinal = ListNode(0, head)
        predecessor = sentinal

        while head:
            if head.next and head.next.val == head.val:
                while head.next and head.next.val == head.val:
                    head = head.next
                predecessor.next = head.next
            else:
                predecessor = predecessor.next
            head = head.next
        return sentinal.next