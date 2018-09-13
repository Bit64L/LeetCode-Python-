class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        for i in range(len(s)):
        	ans += (ord(s[i]) - ord('A') + 1) * (26 ** ( len(s) - 1 - i))
        return ans

solution = Solution()
print(solution.titleToNumber("AD"))