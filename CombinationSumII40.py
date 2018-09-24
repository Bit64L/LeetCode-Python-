# encoding=utf8
class Solution:

    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()

        self.ans = []

        def help(work, candidates, target, path):
            if target == 0:
                self.ans.append(list(path))
                return

            if target < 0 or len(candidates) == 0:
                return

            for i in range(work, len(candidates)):
                if i > work and candidates[i] == candidates[i - 1]:
                    continue
                path.append(candidates[i])
                help(i + 1, candidates, target - candidates[i], path)
                path.pop()

        help(0, candidates, target, [])

        return self.ans

solution = Solution()
print(solution.combinationSum2([1, 1, 2, 5, 6, 7, 10], 8))


# Don't know python data structure well
# 内部函数使用外部函数的变量如何解决: 使用类变量或者传参
# 注意去重的方法
