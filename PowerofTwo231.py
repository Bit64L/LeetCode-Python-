class Solution:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        lo = 0
        high = (int(len(str(n)) / 3) + 1) * 10
        while lo <= high:
        	mid = int((lo + high) / 2)
        	print(mid)
        	if 2 ** mid == n:
        		return True
        	elif 2 ** mid > n:
        		high = mid - 1
        	elif 2 ** mid < n:
        		lo = mid + 1
       	return False


# 利用位运算更简单

solution = Solution()
print(solution.isPowerOfTwo(1))