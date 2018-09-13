class NumArray1:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.dp = [[0] * len(nums) for i in range(len(nums))]

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if i == j:
            self.dp[i][j] = self.nums[i]
            return self.nums[i]
        if self.dp[i][j] != 0:
            return self.dp[i][j]

        sum = self.sumRange(i, j - 1) + self.nums[j]
        self.dp[i][j] = sum
        return sum


# Your NumArray object will be instantiated and called as such:
# obj = NumArray1([-2, 0, 3, -5, 2, -1])
# print(obj.sumRange(0, 0))
# print(obj.sumRange(2, 5))
# print(obj.sumRange(0, 5))
# for i in range(len(obj.nums)):
#     for j in range(len(obj.nums)):
#         print(obj.dp[i][j], end=" ")
#     print()


class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        if nums is None or len(nums) == 0:
            return
        self.nums = nums
        self.dp = [0] * len(nums)
        self.dp[0] = nums[0]
        for i in range(1, len(nums)):
            self.dp[i] = self.dp[i - 1] + nums[i]

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.dp[j] - self.dp[i] + self.nums[i]


obj = NumArray([[[]]])
print(obj.sumRange(0, 0))
print(obj.sumRange(2, 5))
print(obj.sumRange(0, 5))