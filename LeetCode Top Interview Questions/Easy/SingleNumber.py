'''
LeetCode 136. Single Number
Language : Python
'''

from collections import Counter

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
    # 1. Use Counter
    #     tmp = Counter(nums)
    #     items = tmp.items()
    #
    #     for key, val in items:
    #         if val == 1:
    #             answer = key
    #             break
    #
    #     return answer

    # 2. Use XOR
        answer = 0

        for num in nums:
            answer ^= num

        return answer