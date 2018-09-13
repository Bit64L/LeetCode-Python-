class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        pocket = set()
        for i in nums:
        	if i in pocket:
        		return True
        	pocket.add(i)
        return False

solution = Solution()
print(solution.containsDuplicate([1,2,3,4]))