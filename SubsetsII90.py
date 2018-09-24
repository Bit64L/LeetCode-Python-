class Solution:

    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        ans = []

        def helper(work, ans, nums, path):
            ans.append(list(path))
            if work == len(nums):
                return
            for i in range(work, len(nums)):
                if i > work and nums[i] == nums[i - 1]:
                    continue
                path.append(nums[i])
                helper(i + 1, ans, nums, path)
                path.pop()
        helper(0, ans, nums, [])
        return ans

solution = Solution()
print(solution.subsetsWithDup([4, 4, 4, 1, 4]))
