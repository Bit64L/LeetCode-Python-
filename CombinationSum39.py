class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = []

        def helper(curr, candidates, p, target):
            if target <= 0 or len(candidates) == 0:
                if target == 0:
                    ans.append(list(curr))
                return

            for i in range(len(candidates)):
                if i < p:
                    continue
                curr.append(candidates[i])
                helper(curr, candidates, i, target - candidates[i])
                curr.pop()

        helper([], candidates, 0, target)
        return ans


soluton = Solution()
print(soluton.combinationSum([1,2,3], 7))
