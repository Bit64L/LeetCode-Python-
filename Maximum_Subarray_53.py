class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = [0] * len(nums)
        sum[0] = nums[0]
        ans = sum[0]
        for i in range(1, len(nums)):
            sum[i] = (sum[i - 1] + nums[i]) if (sum[i - 1] + nums[i]) > nums[i] else nums[i]
            ans = max(ans, sum[i])
        return ans


solution = Solution()
print(solution.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))

