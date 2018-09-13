import math
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0
        isPrime = [True] * n

        isPrime[0] = False
        isPrime[1] = False
        sn = int(math.sqrt(n)) + 1
        for i in range(2, sn):
            if isPrime[i]:
                j = i
                while True:  # for j in range(i, n) 会报TEL， 推测range函数耗时
                    fx = i * j
                    if fx >= n:
                        break
                    isPrime[fx] = False
                    j += 1

        return sum(isPrime)

solution = Solution()
print(solution.countPrimes(1500000))

