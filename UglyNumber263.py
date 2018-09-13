class Solution:
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        while num % 2 == 0 or num % 3 == 0 or num % 5 == 0:
            if num % 2 == 0:
                num /= 2
            elif num % 3 == 0:
                num /= 3
            elif num % 5 == 0:
                num /= 5
        if num == 1:
            return True
        return False


solution = Solution()
print(solution.isUgly(14))
