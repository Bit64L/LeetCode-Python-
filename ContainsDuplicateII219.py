class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        mapping = {}
        ans = 0
        for i in range(len(nums)):
        	tmp = mapping.get(nums[i], [])
        	tmp.append(i)
        	mapping[nums[i]] = tmp
        for key,val in mapping.items():
        	for i in range(len(val)):
        		for j in range(i + 1, len(val)):
        			if val[j] - val[i] <= k:
        				return True
        return False

solution = Solution()
print(solution.containsNearbyDuplicate([1,2,3,1,2,3],  2))