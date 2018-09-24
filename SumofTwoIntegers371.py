# encoding=utf8
class Solution(object):

    def getSum(self, a, b):
        if b == 0:
            return a
        s = a ^ b
        offset = (a & b) << 1
        s += offset  # use +=
        return s

    def getSum1(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        MASK = 0x100000000
        MAX_INT = 0x7fffffff
        MAX_INT = 0x8fffffff
        while True:
            sum_ = (a ^ b) % MASK
            count = ((a & b) << 1) % MASK
            str = bin(sum_)
            print(str, bin(count), int(str[2:], 2))
            if count == 0:
                break
            a, b = sum_, count

        return sum_ if sum_ <= MAX_INT else (~0 << 31) | sum_


solution = Solution()
print(solution.getSum(-12, -8))

# 1. Python的整数类型为可变32位，用模将其限制在32位
# 2. (~0 << 31) | sum_ 可以正确转换为负数
