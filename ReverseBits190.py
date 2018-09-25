class Solution:
    # @param n, an integer
    # @return an integer

    def reverseBits(self, n):
        result = 0
        for i in range(32):
            result <<= 1
            result |= n & 0x01
            n >>= 1
        return result
solution = Solution()
print(solution.reverseBits(8))
print(len("10000000000000000000000000000"))

# a & 0x01 获得a的最后一位
