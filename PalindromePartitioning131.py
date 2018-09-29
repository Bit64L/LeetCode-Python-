# encoding=utf8
class Solution:

    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        ans = []

        def helper(s, tmp):
            if len(s) == 0:
                ans.append(list(tmp))
                return
            for i in range(len(s)):
                left = s[0:i + 1]
                if left == left[::-1]:
                    tmp.append(left)
                    right = s[i + 1:]
                    helper(right, tmp)
                    tmp.pop()
        helper(s, [])
        return ans

solution = Solution()
print(solution.partition('bb'))

# 这里外部变量ans可以被内部函数使用
