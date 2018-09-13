class Solution:

    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 1 or n == 1:
            return 1 
        
        dp = [[0] * (n + 1) for i in range(m + 1)]
        dp[1][2] = 1
        dp[2][1] = 1
        for i in range(1, m+1):
            for j in range(1, n+1):
                if dp[i][j] != 0:
                    continue
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[m][n]

    
    def uniquePaths1(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        direct = [[1, 0], [0, 1]]
        x, y, self.count = 0, 0, 0

        def countPath(x, y, direct, m, n):
            if x >= m or y >= n:
                return
            if x == m - 1 and y == n - 1:
                self.count += 1
            for i in direct:
                countPath(x + i[0], y + i[1], direct, m, n)

        countPath(0, 0, direct, m, n)
        return self.count




solution = Solution()
print(solution.uniquePaths(1, 2))
