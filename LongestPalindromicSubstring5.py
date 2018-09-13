class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = ""
        for i in range(len(s)):
            for j in range(len(s)):
                sub_str = s[i: j + 1]
                if sub_str == sub_str[::-1] and len(sub_str) > len(ans):
                        ans = sub_str
        return ans


solution = Solution()
print(solution.longestPalindrome("babad"))

