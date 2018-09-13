class Solution:
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s is None or len(s) == 0:
            return 0
        n = len(s)
        ans = 0
        for i in range(n):
            for j in range(i, n):
                sub_str = s[i: j + 1]
                if sub_str == sub_str[::-1]:
                    ans += 1
        return ans


solution = Solution()
print(solution.countSubstrings('aaa'))
