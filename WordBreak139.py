class Solution(object):

    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        memo = (len(s) + 1) * [False]
        memo[0] = True

        for i in range(1, len(s) + 1):
            for j in range(0, i):
                if memo[j] and s[j:i] in wordDict:
                    memo[i] = True
                    break
        return memo[-1]

solution = Solution()
print(solution.wordBreak("applepenap2ple", ['pen', 'apple']))

# 状态转移方程
# dp[i] = dp[j] && (s[j:i] in dict)
