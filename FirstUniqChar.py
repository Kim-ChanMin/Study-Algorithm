'''
LeetCode 387. First Unique Character in a String
Language : Python
'''

# Use Counter
from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        c = Counter(s)

        for idx, char in enumerate(s):
            if c[char] == 1:
                return idx

        return -1