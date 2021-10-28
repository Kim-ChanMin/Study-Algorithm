'''
LeetCode 169. Majority Element
Language : Python
'''

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
    # 1. Brute Force
        # nums.sort()
        # return nums[len(nums)//2]

    # 2. Boyer–Moore Majority Vote Algorithm
        answer = 0
        count = 0

        for num in nums:
            if count == 0:
                answer = num
            if answer != num:
                count -= 1
            else:
                count += 1

        return answer