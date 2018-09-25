class Solution(object):

    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        ans = []

        def helper(work, k, n, ans, path):
            if k == 0:
                if n == 0:
                    ans.append(list(path))
                return
            for i in range(work, 10):
                path.append(i)
                helper(i + 1, k - 1, n - i, ans, path)
                path.pop()
        helper(1, k, n, ans, [])
        return ans
solution = Solution()
print(solution.combinationSum3(3, 15))
