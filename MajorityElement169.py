class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mapping = {}
        for i in nums:
        	count = mapping.get(i, 0)
        	count += 1
        	mapping[i] = count
        	if count > int(len(nums)/ 2):
        		return i
        return None


solution = Solution()
print(solution.majorityElement([3, 2, 3]))