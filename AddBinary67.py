class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        len_a = len(a) - 1
        len_b = len(b) - 1
        c = ""
        accu, i = 0, 0
        while len_a >= 0 or len_b >= 0:
        	if len_a >= 0 and len_b >= 0:
        		sum_ = int(a[len_a]) + int(b[len_b]) + accu
        	else:
        		if len_a >= 0:
        			sum_ = int(a[len_a]) + accu
        		else:
        			sum_ = int(b[len_b]) + accu
        	digit = sum_ % 2
        	accu = int(sum_ / 2)
        	c += str(digit)
        	len_a -= 1
        	len_b -= 1
        if accu != 0:
        	c += str(accu)
        return c[::-1]


solution = Solution()
print(solution.addBinary("1","11"))