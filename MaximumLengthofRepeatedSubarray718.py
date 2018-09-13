class Solution:
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        if A is None or len(A) == 0 or B is None or len(B) == 0:
            return 0

        dp = [[0] * len(B) for i in range(len(A))]

        for i in range(len(A)):
            if B[0] == A[i]:
                dp[i][0] = 1
        for j in range(len(B)):
            if A[0] == B[j]:
                dp[0][j] = 1

        max_val = 0
        for i in range(1, len(A)):
            for j in range(1, len(B)):
                if A[i] == B[j]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    max_val = max(max_val, dp[i][j])
                else:
                    dp[i][j] = 0
        return max_val


solution = Solution()
print(solution.findLength([0, 1, 1, 1, 1], [1, 0, 1, 1, 1]))
# print(solution.findLength([0, 1], [1, 0]))
