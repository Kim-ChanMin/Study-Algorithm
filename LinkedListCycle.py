'''
LeetCode 141. Linked List Cycle
Language : Python
'''

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
    # Floyd’s Cycle Detection Algorithm
        fast, slow = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if fast is slow:
                return True

        return False