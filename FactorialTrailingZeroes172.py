class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count,i, base = 0, 1, 5
        while True:
        	if n == 0:
        		break
        	count += int(n / 5)
        	n /= 5
        return count

solution = Solution()
print(solution.trailingZeroes(30))