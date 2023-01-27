# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def addNumbers(l1, l2, sum, carry):
            if not l1 and not l2:
                if carry != 0:
                    sum.next = ListNode(carry)
                return
            elif l1 and not l2:
                new_sum, new_carry = (l1.val + carry) % 10, (l1.val + carry) // 10
                sum.next = ListNode(new_sum)
                addNumbers(l1.next, l2, sum.next, new_carry)
            elif l2 and not l1:
                new_sum, new_carry = (l2.val + carry) % 10, (l2.val + carry) // 10
                sum.next = ListNode(new_sum)
                addNumbers(l1, l2.next, sum.next, new_carry)
            else:
                new_sum, new_carry = (l1.val + l2.val + carry) % 10, (l1.val + l2.val + carry) // 10
                sum.next = ListNode(new_sum)
                addNumbers(l1.next, l2.next, sum.next, new_carry)
        sum = ListNode()
        carry = 0
        if not l1:
            return l2
        if not l2:
            return l1
        addNumbers(l1,l2, sum, 0)
        return sum.next