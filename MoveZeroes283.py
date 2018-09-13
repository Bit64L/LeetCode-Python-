# class Solution:
#     # def moveZeroes(self, nums):
#     #     """
#     #     :type nums: List[int]
#     #     :rtype: void Do not return anything, modify nums in-place instead.
#     #     """
#     #     i = 0
#     #     n = len(nums)
#     #     while i < n:
#     #         if nums[i] != 0:
#     #             for j in range(i,0,-1):
#     #                 if nums[j - 1]:
#     #                     break
#     #                 tmp = nums[j]
#     #                 nums[j] = nums[j - 1]
#     #                 nums[j - 1] = tmp
#     #         i += 1
#     #     print(nums)
class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j], nums[i] = nums[i], nums[j]
                j += 1
            print(nums, i,j)
        print(nums)

solution = Solution()
print(solution.moveZeroes([1,0,1,1]))
