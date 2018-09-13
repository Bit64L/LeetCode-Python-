class Solution:
    def climbStairs(self, n):
        ans = [0] * (n+1)
        ans[0] = 1
        ans[1] = 1
        for i in range(2, n + 1):
            ans[i] = ans[i - 1] + ans[i - 2]
        return ans[n]

    def climbStairs1(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n == 2:
            return 2

        return self.climbStairs(n - 1) + self.climbStairs(n - 2)


solution = Solution()
print(solution.climbStairs(35))
