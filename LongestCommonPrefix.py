'''
LeetCode 14. Longest Common Prefix
Language : Python
'''

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        answer = ""

        if len(strs) == 0:
            return answer

        strs.sort(key=lambda x: len(x))

        for i in range(len(strs[0])):
            for j in range(1, len(strs)):
                if strs[0][i] != strs[j][i]:
                    return strs[0][:i]
        return strs[0]