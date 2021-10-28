'''
LeetCode 191. Number of 1 Bits
Language : Python
'''

class Solution:
    def hammingWeight(self, n: int) -> int:
    # 1. Use Bit Operators
        count = 0

        for _ in range(32):
            count += (n & 1) == 1
            n >>= 1

        return count
    # 2. Use Built-in modules
    #   return bin(n)[2:].count('1')