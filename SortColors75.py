
# coding=utf-8
class Solution:

    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        self.qsort(nums, 0, len(nums) - 1)

    def qsort(self, nums, lo, high):
        if lo >= high:
            return

        def partition1(nums, lo, high):
            m, p = lo, nums[lo]
            for i in range(lo + 1, high + 1):
                if nums[i] < p:
                    m += 1
                    nums[m], nums[i] = nums[i], nums[m]
            nums[lo], nums[m] = nums[m], nums[lo]
            return m

        def partition2(nums, lo, high):
            i, j, m, p = lo + 1, high, lo, nums[lo]
            while True:
                while i < j and nums[i] < p:
                    i += 1
                while nums[j] > p:
                    j -= 1
                if i >= j:
                    break
                nums[i], nums[j] = nums[j], nums[i]
            nums[m], nums[j] = nums[j], nums[m]
            return j

        p = partition2(nums, lo, high)
        print(p)
        self.qsort(nums, lo, p)
        self.qsort(nums, p + 1, high)

    def bubleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            for j in range(0, len(nums) - i - 1):

                if nums[j] >= nums[j + 1]:
                    tmp = nums[j]
                    nums[j] = nums[j + 1]
                    nums[j + 1] = tmp


solution = Solution()
nums = [2, 0, 2, 1, 1, 0]
solution.sortColors(nums)
print(nums)

# self.qsort(nums, lo, p - 1)
# self.qsort(nums, p + 1, high)
# 分割元素nums[p]已经是排好序的，就没有必要继续放入排序过程中
# 试想如果p是最大的元素的下标, lo也是最大元素的下标，程序将陷入死循环
