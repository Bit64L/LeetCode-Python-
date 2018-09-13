class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if grid is None or len(grid) == 0:
            return 0
        import sys
        dp = [[sys.maxsize] * (len(grid[0]) + 1) for i in range(len(grid) + 1)]
        for i in range(1, len(grid) + 1):
            for j in range(1, len(grid[0]) + 1):
                if i == 1 and j == 1:
                    dp[i][j] = grid[i-1][j-1]
                    continue
                dp[i][j] = grid[i - 1][j - 1] + min(dp[i - 1][j], dp[i][j - 1])
        return dp[len(grid)][len(grid[0])]


solution = Solution()
print(solution.minPathSum([
    [1, 3, 1],
]))
