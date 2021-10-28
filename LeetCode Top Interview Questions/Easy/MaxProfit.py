'''
LeetCode 121. Best Time to Buy and Sell Stock
Language : Python
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 0:
            return 0
        # Use Kadane's Algorithm
        answer, cur = 0, 0

        for i in range(1, len(prices)):
            cur = max(cur + (prices[i] - prices[i - 1]), 0)
            answer = max(answer, cur)

        return answer