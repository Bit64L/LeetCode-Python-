class Solution:
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) < 3:
            return 0
        n, ans = 2, 0

        for i in range(2, len(A)):
            if A[i] - A[i - 1] == A[i - 1] - A[i - 2]:
                n += 1
                ans += n - 2
            else:
                n = 2
        return ans


solution = Solution()
print(solution.numberOfArithmeticSlices([1, 2, 3, 4, 5]))
