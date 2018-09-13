class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s is None or s == '':
            return 0
        i = 0
        j = 1
        ans = j - i
        box = set()
        box.add(s[i])
        while i <= j < len(s):
            if s[j] in box:
                box.remove(s[i])
                i = i + 1
            else:
                box.add(s[j])
                j = j + 1
                ans = max(ans, j - i)
        return ans


solution = Solution()
print(solution.lengthOfLongestSubstring('pwwwkceew'))
