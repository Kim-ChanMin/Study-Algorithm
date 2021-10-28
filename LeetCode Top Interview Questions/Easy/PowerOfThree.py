'''
LeetCode 326. Power of Three
Language : Python
'''

# 1. Iteratively
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        while n > 1:
            if n % 3 != 0:
                return False
            else:
                n //= 3

        return True

#2. Recursively
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1:
            return True

        elif n <= 0:
            return False

        if n % 3 != 0:
            return False

        else:
            return self.isPowerOfThree(n // 3)