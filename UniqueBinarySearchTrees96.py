class Solution(object):

    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        nums = [0] * (n + 1)
        nums[0] = 1
        nums[1] = 1

        for i in range(2, n + 1):
            for j in range(0, i):
                nums[i] += nums[j] * nums[i - j - 1]
        return nums[n]

    def numTrees1(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1
        if n == 1:
            return 1
        result = 0
        for i in range(1, n + 1):
            result += self.numTrees(i - 1) * self.numTrees(n - i)
        return result


solution = Solution()
print(solution.numTrees(3))
