class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        nums = list(range(1, n+1))
        self.ans = []
        self.k = k
        helper(nums, layer, single):
        	if layer == self.k:
        		self.ans.append(list(single))
        		return 
        	for num in nums:
        		single.append(num)
        		pocket = set(nums)
        		pocket.remove(num)
        		helper(pocket, layer + 1, single)
        		single.pop()
        helper(nums, 1, [])
        return self.ans

solution = Solution()
print(solution.combine(4, 2))