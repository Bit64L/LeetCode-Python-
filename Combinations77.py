class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        nums = list(range(1, n + 1))
        self.ans = []
        self.k = k
        def helper(nums, layer, single):
            if layer == self.k:
                self.ans.append(list(single))
                return
            for i in range(len(nums)):
                single.append(nums[i])
                helper(nums[i+1:], layer + 1, single)
                single.pop()

        helper(nums, 0, [])
        return self.ans


solution = Solution()
print(solution.combine(0, 0))
