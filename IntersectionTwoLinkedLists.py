'''
LeetCode 160. Intersection of Two Linked Lists
Language : Python
'''

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None

        a = headA
        b = headB

        while a != b:
            if a is None:
                a = headB
            else:
                a = a.next
            if b is None:
                b = headA
            else:
                b = b.next

        return a