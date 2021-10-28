'''
LeetCode 217. Contains Duplicate
Language : Python
'''

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
    # 1. Use Set
        return len(set(nums)) != len(nums)
    # 2. Use Counter
    # tmp = Counter(nums)
    #
    # for i, j in tmp.items():
    #     if j >= 2:
    #         return True
    #
    # return False
