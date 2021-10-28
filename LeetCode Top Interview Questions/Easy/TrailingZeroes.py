'''
LeetCode 172. Factorial Trailing Zeroes
Language : Python
'''

class Solution:
    def trailingZeroes(self, n: int) -> int:
        answer = 0

        while n:
            n //= 5
            answer += n

        return answer