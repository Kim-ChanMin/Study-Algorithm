'''
LeetCode 53. Maximum Subarray
Language : Python
'''

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 1. Divide And Conquer
        # def divideAndConquer(self, nums, start, end):
        #     if start == end:
        #         return nums[start]
        #
        #     mid = (start + end) // 2
        #     # Left part
        #     Lmax = divideAndConquer(self, nums, start, mid)
        #     # Right part
        #     Rmax = divideAndConquer(self, nums, mid + 1, end)
        #     sum_tmp, left, right = 0, float('-inf'), float('-inf')
        #
        #     # Find maximum subarray in left side
        #     for i in range(mid, start - 1, -1):
        #         sum_tmp += nums[i]
        #         left = max(left, sum_tmp)
        #     sum_tmp = 0
        #     # Find maximum subarray in right side
        #     for j in range(mid + 1, end + 1):
        #         sum_tmp += nums[j]
        #         right = max(right, sum_tmp)
        #     return max(Lmax, Rmax, left + right)
        #
        # answer = divideAndConquer(self, nums, 0, len(nums) - 1)
        # return answer

        # 2. Kadane's Algorithm
        for num in range(1, len(nums)):
            if nums[num - 1] > 0:
                nums[num] += nums[num - 1]

        return max(nums)