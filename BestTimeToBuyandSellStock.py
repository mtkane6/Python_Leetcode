class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0

    # buy is the low, sell is the high point
        buy, maxProfit = float('inf'), 0
        for i in range(0, len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            else:
                if (prices[i] - buy) > maxProfit:
                    maxProfit = prices[i] - buy
        return maxProfit