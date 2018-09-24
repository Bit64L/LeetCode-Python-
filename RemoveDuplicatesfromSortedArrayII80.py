class Solution(object):

    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return 0
        curr, count = 0, 0
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                count += 1
            else:
                count = 1
            if count <= 2:
                nums[curr] = nums[i]
                curr += 1
        return curr

solution = Solution()
print(solution.removeDuplicates([1, 2, 2, 2, 2, 3, 3, 3, 4, 5]))
