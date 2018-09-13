class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        diff = 0xffff
        ans = 0xffff
        n = len(nums)
        for i in range(n - 2):
        	if i > 0 and nums[i] == nums[i-1]:
        		continue
        	j, k = i+1, n - 1
        	while j < k:
        		s = nums[i] + nums[j] + nums[k]
        		if abs(s - target) < diff:
        			diff = abs(s - target)
        			ans = s
        		if s > target:
        			k -= 1
        		elif s < target:
        			j += 1
        		else:
        			return target
        return ans

solution = Solution()
print(solution.threeSumClosest( [-1, 2, 1, -4], 1))
