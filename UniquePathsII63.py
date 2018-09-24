# encoding=utf8
class Solution:

    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if obstacleGrid is None or len(obstacleGrid) == 0:
            return 0
        if len(obstacleGrid) == 1:
            if sum(obstacleGrid[0]) == 0:
                return 1
            else:
                return 0
        dp = [[0] * len(obstacleGrid[0]) for i in range(len(obstacleGrid))]
        dp[0][0] = 1
        for i in range(0, len(obstacleGrid)):
            for j in range(0, len(obstacleGrid[0])):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                    continue
                if i > 0:
                    dp[i][j] += dp[i - 1][j]
                if j > 0:
                    dp[i][j] += dp[i][j - 1]
        return dp[len(obstacleGrid) - 1][len(obstacleGrid[0]) - 1]

    def uniquePathsWithObstacles1(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """

        if obstacleGrid is None or len(obstacleGrid) == 0:
            return 0
        if len(obstacleGrid) == 1:
            if sum(obstacleGrid[0]) == 0:
                return 1
            else:
                return 0

        direction = [[0, 1], [1, 0]]
        self.ans = 0

        def helper(x, y, direction, obstacleGrid):
            if x < 0 or y < 0 or x >= len(obstacleGrid) or y >= len(obstacleGrid[0]):
                return
            if obstacleGrid[x][y] == 1:
                return
            if x == len(obstacleGrid) - 1 and y == len(obstacleGrid[0]) - 1:
                self.ans += 1
                return
            for direct in direction:
                x += direct[0]
                y += direct[1]
                helper(x, y, direction, obstacleGrid)
                x -= direct[0]
                y -= direct[1]
        helper(0, 0, direction, obstacleGrid)
        return self.ans

solution = Solution()
print(solution.uniquePathsWithObstacles(
    [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
))

# sum不能直接计算多为list
