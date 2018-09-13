class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums or len(nums) == 0:
        	return []

        mapping = {}
        ans = []
        for i in range(len(nums)):
        	diff = target - nums[i]
        	if diff in mapping.keys():
        		return [mapping[diff], i]
        	mapping.update({nums[i]: i})
        return []
 

solution = Solution()
print(solution.twoSum([2, 7, 11, 15], 9))