# class Solution:
#     def canWinNim(self, n):
#         """
#         :type n: int
#         :rtype: bool
#         """
#         dp = [True, True, True, True, False]
#         if n <= 4:
#             return dp[n]
#         for i in range(5, n + 1):
#             willWin = False
#             for j in [1, 2, 3]:
#                 if dp[i - j] == False:
#                     dp.append(True)
#                     willWin = True
#                     break
#             if not willWin:
#                 dp.append(False)
#         print(dp)
#         return dp[n]
class Solution:
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n % 4 == 0:
            return False
        return True

solution = Solution()
print(solution.canWinNim(6))
