'''
LeetCode 20. Valid Parentheses
Language : Python
'''

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket = {'}': '{', ')': '(', ']': '['}

        for ch in s:
            if ch in bracket.values():
                stack.append(ch)
            else:
                if stack and bracket[ch] == stack[-1]:
                    stack.pop()
                else:
                    return False

        if stack:
            return False

        return True