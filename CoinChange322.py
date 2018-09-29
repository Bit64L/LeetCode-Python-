# encoding=utf8
class Solution(object):

    def coinChange1(self, coins, amount):  # TLE
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        coins.sort(reverse=True)
        self.ans = -1

        def helper(coins, amount, tmp):
            if self.ans != -1:
                return
            if amount == 0:
                self.list.append(list(tmp))
                self.ans = len(tmp)
                return
            if amount < 0:
                return
            for coin in coins:
                tmp.append(coin)
                helper(coins, amount - coin, tmp)
                tmp.pop()
        self.list = []
        helper(coins, amount, [])
        print(self.list)
        return self.ans

     def coinChange1(self, coins, amount):  # 改造为带返回值的递归 
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        self.ans = -1

        def helper(coins, amount, tmp):
            if self.ans != -1:
                return
            if amount == 0:
                self.list.append(list(tmp))
                self.ans = len(tmp)
                return
            if amount < 0:
                return
            for coin in coins:
                tmp.append(coin)
                count = 1+helper(coins, amount - coin, tmp)
                tmp.pop()
        self.list = []
        helper(coins, amount, [])
        print(self.list)
        return self.ans

solution = Solution()
print(solution.coinChange([1, 2, 5], 11))
print(solution.coinChange([186, 419, 83, 408], 6249))

# ans为非引用类型，不能供内部函数使用，可转变为类属性使用
