class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        d = dict()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                sum1 = nums[i] + nums[j]
                if sum1 in d:
                    d[sum1].append((i, j))
                else:
                    d[sum1] = [(i, j)]
        ans = set()
        for key in d:
            value = target - key
            if value in d:
                list1 = d[key]
                list2 = d[value]
                for (i, j) in list1:
                    for (k, l) in list2:
                        if i != k and i != l and j != k and j != l:
                            tmp = [nums[i], nums[j], nums[k], nums[l]]
                            tmp.sort()
                            ans.add(tuple(tmp))
        return list(ans)


solution = Solution()
print(solution.fourSum([1, 0, -1, 0, -2, 2], 0))
