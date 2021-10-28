'''
LeetCode 13. Roman To Integer
Language : Python
'''

class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
        answer = 0

        for i in range(len(s) - 1):
            if dic[s[i]] < dic[s[i + 1]]:
                answer -= dic[s[i]]
            else:
                answer += dic[s[i]]
        answer += dic[s[-1]]

        return answer