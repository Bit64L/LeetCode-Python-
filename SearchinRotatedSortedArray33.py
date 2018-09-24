class Solution(object):

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return -1
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return mid
            if target < nums[mid]:
                if nums[mid] <= nums[hi]:
                    hi = mid - 1
                else:
                    if target >= nums[lo]:
                        hi = mid - 1
                    else:
                        lo = mid + 1
            else:
                if nums[lo] <= nums[mid]:
                    lo = mid + 1
                else:
                    if target <= nums[hi]:
                        lo = mid + 1
                    else:
                        hi = mid - 1
        if target == nums[lo]:
            return lo
        return -1

solution = Solution()
print(solution.search([], 8))

# mid分割的两部分，必然有一边是有序的
