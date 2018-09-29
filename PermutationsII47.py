# encoding=utf8


class Solution:

    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        mark = [0] * len(nums)
        nums.sort()  # remove duplicate

        def helper(work, nums, ans, path, mark):
            if len(path) == len(nums):
                ans.append(list(path))
                return
            for i in range(0, len(nums)):
                if mark[i] == 1:
                    continue
                # remove duplicate
                if i > 0 and nums[i] == nums[i - 1] and mark[i - 1] == 1:
                    print(path)
                    continue

                path.append(nums[i])
                mark[i] = 1
                helper(work + 1, nums, ans, path, mark)
                mark[i] = 0
                path.pop()
        ans = []
        helper(0, nums, ans, [], mark)
        return ans

solution = Solution()
print(solution.permuteUnique([1, 1, 2]))

# 排列去重(排序+work指针， 或者标记数组)
# 全排列 全排列去重
