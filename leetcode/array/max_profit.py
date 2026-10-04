class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        l, r = 0, 1
        maxP = 0

        while r < n:
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r
            r += 1

        return maxP
