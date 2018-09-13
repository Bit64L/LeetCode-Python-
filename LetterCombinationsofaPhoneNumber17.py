class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits is None or len(digits) == 0:
        	return []
        mapping = {                 
        	"2" : 'abc',
        	"3" : 'def',
        	"4" : 'ghi',
        	"5" : 'jkl',
        	"6" : 'mno',
        	"7" : 'pqrs',
        	"8" : 'tuv',
        	"9" : 'wxyz'
        }
        ans = []
        self.findCombination(digits, ans, '',mapping)
        return ans

    def findCombination(self, digits, ans, tmp, mapping):
    		if len(digits) == 0:
    			ans.append(tmp)
    			return 
    		str_ = mapping.get(digits[0])
    		for j in str_:
    			tmp += j
    			self.findCombination(digits[1:], ans, tmp, mapping)
    			tmp = tmp[0:len(tmp)-1]


solution = Solution()
print(solution.letterCombinations(""))