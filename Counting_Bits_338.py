import math


class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        if num is None or num == 0:
            return [0]
        dp = [0] * (num + 1)
        dp[0], dp[1] = 0, 1
        if num == 1:
            return [0, 1]
        for i in range(2, num + 1):
            start_expo = int(math.log(i, 2))
            start_value, end_value = 2 ** start_expo, 2 ** (start_expo + 1)
            median_value = int((start_value + end_value) / 2)
            if start_value <= i < median_value:
                dp[i] = dp[(2 ** (start_expo - 1) + i % start_value)]
            elif median_value <= i < end_value:
                dp[i] = dp[(2 ** (start_expo - 1) + i % start_value)] + 1
        return dp


solution = Solution()
print(solution.countBits(5))