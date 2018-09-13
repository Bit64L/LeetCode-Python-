class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums or len(nums) == 0:
        	return 0

        low, high = 0, len(nums) - 1
        while low <= high:
        	mid = int((low + high) / 2)
        	if nums[mid] > target:
        		high = mid - 1
        	elif nums[mid] < target:
        		low = mid + 1
        	else:
        		return mid
        return high+1

solution = Solution()
print(solution.searchInsert([1,3,5,6], 7))