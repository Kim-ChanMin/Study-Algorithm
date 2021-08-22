'''
LeetCode 9. Palindrome Number
Language : Python
'''

class Solution:
    def isPalindrome(self, x: int) -> bool:
        # 1) Using List
        # num = list(str(x))
        # return num == num[::-1]

        # 2) Without String
        if x < 0:
            return False

        origin = x
        palindrome = 0

        while x > 0:
            palindrome = x % 10 + palindrome * 10
            x //= 10

        return origin == palindrome