'''
LeetCode 118. Pascal's Triangle
Language : Python
'''

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        answer = []

        for i in range(numRows):
            answer.append([])
            for j in range(i + 1):
                if j == 0 or j == i:
                    answer[i].append(1)
                else:
                    answer[i].append(answer[i - 1][j - 1] + answer[i - 1][j])

        return answer