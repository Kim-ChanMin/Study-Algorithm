'''
LeetCode 234. Palindrome Linked List
Language : Python
'''

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
    # 1. Brute Force
    #     answer = []
    #
    #     while head:
    #         answer.append(head.val)
    #         head = head.next
    #     return answer == answer[::-1]
    
    # 2. Optimal
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None

        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

        while prev:
            if prev.val != head.val:
                return False
            prev = prev.next
            head = head.next

        return True

