class Solution:

    def getPermutation(self, n, k):
        import math
        nums = range(1, n + 1)
        ans = ''
        k -= 1
        while n > 0:
            n -= 1
            index, k = divmod(k, math.factorial(n))
            ans += str(nums[index])
            nums.remove(nums[index])
        return ans

    def getPermutation1(self, n, k):  # TLE
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        mark = [0] * (n + 1)

        def helper(mark, n, k, path, ans):
            if len(path) == n:
                ans.append(path)
                return
            if len(ans) == k:
                return
            for i in range(1, n + 1):
                if mark[i] == 0:
                    mark[i] = 1
                    path += str(i)
                    helper(mark, n, k, path, ans)
                    path = path[0:len(path) - 1]
                    mark[i] = 0

        ans = []
        helper(mark, n, k, '', ans)
        return ans[-1]


solution = Solution()
print(solution.getPermutation(1, 1))

# n=4, k = 14 => 3 + permutation(1,2,4)

# 全排列问题： 无重复全排列，有重复全排列，第n个排列，有条件的全排列
