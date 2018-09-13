class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices is None or len(prices) == 0:
            return 0
        ans, minBuy, n = 0, prices[0], len(prices)
        for i in range(n):
            ans = max(ans, prices[i] - minBuy)
            minBuy = min(minBuy, prices[i])
        return ans


solution = Solution()
print(solution.maxProfit([7, 1, 5, 3, 6, 4]))
