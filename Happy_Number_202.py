class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        s = set()

        s.add(n)
        while n != 1:
            n = self.change(n)
            if n in s:
                return False
            s.add(n)
        return True

    def change(self, n):
        sum = 0
        while n > 0:
            sum += (n % 10) * (n % 10)
            n = int(n / 10)
        return sum


solution = Solution()
print(solution.isHappy(19))
