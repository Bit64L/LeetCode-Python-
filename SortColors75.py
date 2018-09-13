class Solution:


	def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
        	for j in range(0, len(nums) - i - 1):
        		
        		if nums[j] >= nums[j+1]:
        			tmp = nums[j]
        			nums[j] = nums[j+1]
        			nums[j+1] = tmp


    def sortColors1(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
        	for j in range(0, len(nums) - i - 1):
        		
        		if nums[j] >= nums[j+1]:
        			tmp = nums[j]
        			nums[j] = nums[j+1]
        			nums[j+1] = tmp



solution = Solution()
print(solution.sortColors([2,0,2,1,1,0]))

