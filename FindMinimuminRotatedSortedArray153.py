class Solution(object):

    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lo, high, n = 0, len(nums) - 1, len(nums) - 1
        if nums[lo] < nums[high]:
            return nums[lo]
        while lo < high:
            mid = (lo + high) // 2
            if mid > 0 and nums[mid - 1] > nums[mid]:
                return nums[mid]
            if mid < n and nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            if nums[lo] <= nums[mid]:
                lo = mid + 1
            else:
                high = mid
        return nums[lo]

    def findMin2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lo, high = 0, len(nums) - 1
        while lo < high:
            if nums[lo] < nums[high]:
                return nums[lo]
            mid = (lo + high) // 2
            if nums[lo] <= nums[mid]:
                lo = mid + 1
            else:
                high = mid
        return nums[lo]

    def findMin1(self, nums):
        if nums[0] <= nums[-1]:
            return nums[0]
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                return nums[i]
        return None


solution = Solution()
print(solution.findMin([4, 5, 6, 1, 2, 3]))
print(solution.findMin1([4, 5, 6, 7, 0, 1, 2]))


# 第一种解法：常规，O(N), O(1)
# 第二种解法： 二分， O(logN), O(1)
