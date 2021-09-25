'''
LeetCode 242. Valid Anagram
Language : Python
'''
from collections import Counter

# 1. Use Counter(1)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        for i in set(s):
            if s.count(i) != t.count(i):
                return False

        return True

# 2. Use Counter(2)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
    	return Counter(s) == Counter(t)

# 3. Use Sorted
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)