class Solution(object):

    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if nums is None or len(nums) == 0:
            return [-1, - 1]
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                i = mid
                while i >= 0 and nums[i] == target:
                    i -= 1
                j = mid
                while j <= len(nums) - 1 and nums[j] == target:
                    j += 1
                return [i + 1, j - 1]
            if target < nums[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        if nums[lo] == target:
            return [lo, lo]
        return [-1, -1]

solution = Solution()
print(solution.searchRange([0], 0))

# 二分搜索的结束条件， lo == hi
# 如果nums[lo] == target， 最后找到
