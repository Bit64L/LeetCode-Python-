class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        import math
        count = abs(n)

        def helper(base, count):
            if count == 0:
                return 1
            if count == 1:
                return base
            if count % 2 == 1:
                ans = helper(base, count - 1) * base
                return ans
            else:
                ans = helper(base, count / 2)
                return ans * ans

        ans = helper(x, count)
        if n < 0:
            return 1.0 / ans
        else:
            return ans

    def pow(self, x, n):
        result = 1
        power = abs(n)
        while power > 0:
            if power % 2 == 1:
                result = result * x
            x = x * x
            power /= 2
        if n > 0:
            return result
        else:
            return 1.0 / result


solution = Solution()
print(solution.pow(3, 5))
print(solution.myPow(3, 5))
