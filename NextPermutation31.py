# encoding=utf8
class Solution(object):

    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if nums is None or len(nums) == 0:
            return
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        j = len(nums) - 1
        while j > i and nums[j] <= nums[i]:
            j -= 1

        if i == -1:
            nums.sort()
            return
        nums[i], nums[j] = nums[j], nums[i]
        nums[i + 1:] = sorted(nums[i + 1:])


solution = Solution()
nums = [1, 5, 1]
solution.nextPermutation(nums)
print(nums)

# 部分排序
# 数组sorted(nums[i + 1:])
