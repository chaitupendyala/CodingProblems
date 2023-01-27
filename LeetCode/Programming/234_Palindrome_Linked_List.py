class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head.next:
            return True
        if not head.next.next:
            if head.val != head.next.val:
                return False
            else:
                return True
        slow, fast = head, head
        while slow.next and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        previous, curr, nxt = None, slow.next, None
        while curr:
            next = curr.next
            curr.next = previous
            previous = curr
            curr = next
        
        while previous and head:
            if previous.val != head.val:
                return False
            previous = previous.next
            head = head.next
        return True