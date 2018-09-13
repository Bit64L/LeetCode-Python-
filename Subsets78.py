class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums is None or len(nums) == 0:
            return []
        nums.sort()
        ans = [[], [nums[0]]]
        pre = nums[0]
        for i in nums:
            j = 0
            n = len(ans)
            if i == pre:
                continue
            else:
                pre = i
            while j < n:
                import copy
                curr = copy.deepcopy(ans[j])
                curr.append(i)
                ans.append(curr)
                j += 1
        return ans


solution = Solution()
print(solution.subsets([-1, 1, 2]))
