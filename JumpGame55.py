class Solution:

    def canJump(self, nums):  # GREEDY
        """
        :type nums: List[int]
        :rtype: bool
        """
        if nums is None or len(nums) <= 1:
            return True
        max_ = 0
        for i in range(0, len(nums) - 1):
            max_ = max(max_, i + nums[i])
            if max_ >= len(nums) - 1:
                return True
            if max_ < i + 1:
                return False
        return False

    def canJump1(self, nums):  # TLE O(n2)
        """
        :type nums: List[int]
        :rtype: bool
        """
        curr, n = 0, len(nums) - 1
        self.ans = False

        def help(curr, n, nums):
            if curr == n:
                self.ans = True
                return
            if curr > n:
                return
            for i in range(1, nums[curr] + 1):
                curr += i
                help(curr, n, nums)
                curr -= i
        help(curr, n, nums)
        return self.ans

solution = Solution()
print(solution.canJump([0]))

# 贪心
