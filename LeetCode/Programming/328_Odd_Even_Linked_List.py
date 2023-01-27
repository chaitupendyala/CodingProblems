from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next or not head.next.next:
            return head
        odd, even = head, head.next
        head2 = head.next
        while odd and even:
            odd.next = even.next
            if odd.next:
                even.next = odd.next.next
            odd = odd.next
            even = even.next
        odd = head
        while odd.next:
            odd = odd.next
        odd.next = head2
        return head

head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))
head = Solution().oddEvenList(head)
while head:
    print(head.val)
    head = head.next