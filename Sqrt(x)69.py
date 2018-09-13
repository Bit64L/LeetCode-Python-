class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        lo, high = 0, x+1
        count = 0
        while lo <= high:
            mid = int((lo + high) / 2)
            if mid * mid > x:
                high = mid - 1
            elif mid * mid < x:
                lo = mid + 1
            else:
                return mid
        return high

solution = Solution()
print(solution.mySqrt(100))
