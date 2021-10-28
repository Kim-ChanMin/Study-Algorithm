'''
LeetCode 268. Missing Number
Language : Python
'''

# 1. Use Sum
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        answer = n * (n + 1) // 2 - sum(nums)

        return answer

# 2. Use Sort
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()

        for num in range(len(nums)):
            if num != nums[num]:
                return num

        return len(nums)