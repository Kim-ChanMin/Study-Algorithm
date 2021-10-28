'''
LeetCode 28. Implement strStr()
Language : Python
'''

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # 1. Brute Force
        #
        # if len(needle) == 0:
        #     return 0
        #
        # for i in range(len(haystack) - len(needle) + 1):
        #     if haystack[i:i + len(needle)] == needle:
        #         return i
        #
        # return -1
        # 2. Use find()
        if not needle:
            return 0
        if needle in haystack:
            return haystack.find(needle)
        else:
            return -1