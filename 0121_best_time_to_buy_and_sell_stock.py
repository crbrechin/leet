class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        beg = 0
        profit = 0

        for end in range(len(prices)):
            profit = max(profit, prices[end] - prices[beg])
            if prices[end] < prices[beg]:
                beg = end

        return profit
