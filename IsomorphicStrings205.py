class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        smapping = {}
        tmapping = {}
        for i in range(len(s)):
            if s[i] not in smapping:
                smapping[s[i]] = -1
            if t[i] not in tmapping:
                tmapping[t[i]] = -1
            if smapping[s[i]] != tmapping[t[i]]:
                return False
            smapping[s[i]] = i
            tmapping[t[i]] = i
        return True

solution = Solution()
print(solution.isIsomorphic("foo", "tdd"))