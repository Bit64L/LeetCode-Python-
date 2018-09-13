class Solution:
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        if len(pattern) != len(str.split(" ")):
        	return False
        pmap = {}
        smap = {}
        for i in range(len(pattern)):
        	ppreIndex = pmap.get(pattern[i], None)
        	pmap[pattern[i]] = i

        	strs = str.split(" ")
        	spreIndex = smap.get(strs[i], None)
        	smap[strs[i]] = i

        	if spreIndex != ppreIndex:
        		return False
        return True

solution = Solution()
print(solution.wordPattern("abbc", "dog cat cat dog"))