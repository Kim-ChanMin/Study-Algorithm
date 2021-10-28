'''
LeetCode 1. Two-sum
Language : Python
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       '''
       # 1. Brute Force
        for i in range(len(nums)) :
            for j in range(i+1, len(nums)) :
                if nums[i] + nums[j] == target :
                    return [i,j]
        '''
       # 2. Hash Map
        dict = {}

        for i, nums in enumerate(nums):
            if target - nums in dict:
                return [dict[target - nums], i]
            dict[nums] = i