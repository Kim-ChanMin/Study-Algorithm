'''
LeetCode 3. Longest Substring Without Repeating Characters
Language : Python
'''

# Use Sliding Window Algorithm
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        tmp = {}
        max_length = start = 0

        for i, j in enumerate(s):
            if j in tmp and start <= tmp[j]:
                start = tmp[j] + 1
            else:
                max_length = max(max_length, i - start + 1)

            tmp[j] = i

        return max_length