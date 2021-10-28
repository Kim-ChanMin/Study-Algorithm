'''
LeetCode 350. Intersection of Two Arrays II
Language : Python
'''

# 1. Use Dictionary
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        tmp = {}
        answer = []

        for i in nums1:
            if i not in tmp:
                tmp[i] = 1
            else:
                tmp[i] += 1

        for i in nums2:
            if i in tmp:
                if tmp[i] > 1:
                    tmp[i] -= 1
                else:
                    del tmp[i]
                answer.append(i)

        return answer

# 2. Use Counter
from collections import Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return (Counter(nums2) & Counter(nums1)).elements()