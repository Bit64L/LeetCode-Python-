class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        for i in range(len(s)):
        	if i != len(s) - 1:
        		if self.isSub(s[i], s[i+1]):
        			ans -= self.convert(s[i])
        		else:
        			ans += self.convert(s[i])
        	else:
        		ans += self.convert(s[i])
        return ans

    def convert(self, r):
    	return {
    		'I': 1,
    		'V': 5,
    		'X': 10,
    		'L': 50,
    		'C': 100,
    		'D': 500,
    		'M': 1000
    	}.get(r)

    def isSub(self, s1, s2):
    	if s1 == 'I':
    		if s2 == 'V' or s2 == 'X':
    			return True
    		return False
    	if s1 == 'X':
    		if s2 == 'L' or s2 == 'C':
    			return True
    		return False
    	if s1 == 'C':
    		if s2 == 'D' or s2 == 'M':
    			return True
    		return False
    	return False


solution = Solution()
print(solution.romanToInt("MCMXCIV"))