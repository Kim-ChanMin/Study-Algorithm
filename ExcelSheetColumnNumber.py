'''
LeetCode 171. Excel Sheet Column Number
Language : Python
'''

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        answer = 0

        for s in columnTitle:
            answer = answer * 26 + ord(s) - ord("A") + 1

        return answer