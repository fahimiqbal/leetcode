class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0

        left = 0
        right = 1

        while right < len(prices):
            if prices[right] < prices[left]:
                left = right
            elif prices[left] < prices[right]:
                if maxProfit < (prices[right] - prices[left]):
                    maxProfit = prices[right] - prices[left]
            right += 1


        return maxProfit