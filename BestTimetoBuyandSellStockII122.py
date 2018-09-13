class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices is None or len(prices) < 2:
        	return 0
        buyDay, ans = 0, 0
        for i in range(1, len(prices)):
        	if prices[i] > prices[i-1]:
        		if i - 1 != buyDay:
        			ans += prices[i] - prices[i-1]
        		else:
        			ans += prices[i] - prices[buyDay]

        	else:
        		buyDay = i
        return ans

solution = Solution()
print(solution.maxProfit([4]))