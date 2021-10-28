'''
LeetCode 202. Happy Number
Language : Python
'''

class Solution:
    def isHappy(self, n: int) -> bool:
        tmp = set()

        while n not in tmp:
            tmp.add(n)
            n = sum([int(x) ** 2 for x in str(n)])

            if n == 1:
                return True

        return False