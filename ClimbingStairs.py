'''
LeetCode 70. Climbing Stairs
Language : Python
'''

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2 :
            return n
        else :
            answer, step_1, step_2 = 0, 1, 2
            for i in range(2, n):
                answer = step_2 + step_1
                step_1 = step_2
                step_2 = answer
            return answer