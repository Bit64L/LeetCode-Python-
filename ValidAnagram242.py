class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        smap, tmap = {}, {}
        for i in range(len(s)):
            count = smap.get(s[i], 0)
            count += 1
            smap[s[i]] = count

            count = tmap.get(t[i], 0)
            count += 1
            tmap[t[i]] = count

        for key, val in smap.items():
            if tmap.get(key, None) != val:
                return False
        return True


solution = Solution()
print(solution.isAnagram("car", "rat"))
