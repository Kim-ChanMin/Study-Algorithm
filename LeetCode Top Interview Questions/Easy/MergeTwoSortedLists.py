'''
LeetCode 21. Merge Two Sorted Lists
Language : Python
'''

class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        if l1 is None:
            return l2
        if l2 is None:
            return l1

        if l1.val < l2.val:
            head = ListNode(l1.val)
            head.next = self.mergeTwoLists(l1.next, l2)
        else:
            head = ListNode(l2.val)
            head.next = self.mergeTwoLists(l1, l2.next)

        return head
