class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        n = len(nums)
        ans = []

        for i in range(0, n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j,k = i + 1, n - 1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s > 0:
                    k -= 1
                elif s < 0:
                    j += 1
                else:
                    ans.append([nums[i], nums[j], nums[k]])
                    while j<k and nums[j] == nums[j+1]:
                        j += 1
                    while j<k and nums[k] == nums[k-1]:
                        k -= 1
                    j, k = j+1, k-1
        return ans

solution = Solution()
print(solution.threeSum( [-1, 0, 1, 2, -1, -4]))
