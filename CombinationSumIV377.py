class Solution(object):

    def combinationSum4(self, nums, target):  # dp, bottom to top
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(1, target + 1):
            for num in nums:
                if i - num >= 0:
                    dp[i] += dp[i - num]
        return dp[target]

    def combinationSum42(self, nums, target):  # dp, top to bottom
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dp = [-1] * (target + 1)

        def helper(nums, target):
            if target == 0:
                return 1
            if target < 0:
                return 0
            if dp[target] != -1:
                return dp[target]
            ans = 0
            for num in nums:
                ans += helper(nums, target - num)  # recursion formula
            dp[target] = ans
            return ans

        return helper(nums, target)

    def combinationSum41(self, nums, target):  # regular recursion
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def helper(nums, target):
            ans = 0
            if target == 0:
                return 1
            if target < 0:
                return 0
            for num in nums:
                ans += helper(nums, target - num)  # recursion formula
            return ans

        return helper(nums, target)


solution = Solution()
print(solution.combinationSum42([1, 2, 3], 4))
