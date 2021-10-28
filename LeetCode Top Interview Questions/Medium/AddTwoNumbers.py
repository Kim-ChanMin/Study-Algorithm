'''
LeetCode 2. Add Two Numbers
Language : Python
'''

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        answer = head = ListNode(0)
        carry = 0

        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next

            head.next = ListNode(carry % 10)
            head = head.next
            carry //= 10

        return answer.next