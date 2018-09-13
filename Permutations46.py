class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums is None or len(nums) == 0:
            return []
        ans = []

        def findCombination(tmp, nums):
            if len(nums) == 0:
                ans.append(list(tmp))
                return
            for i in nums:
                sc = set(nums)
                sc.remove(i)
                tmp.append(i)
                findCombination(tmp, sc)
                tmp.pop()

        findCombination([], nums)
        return ans

    

solution = Solution()
print(solution.permute([1,2,3]))