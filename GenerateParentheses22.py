class Solution:

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []
        if n == 0:
            return ans

        def helper(path, ans, left, right, n):
            if left == n and right == n:
                ans.append(path)
                return
            if left < n:
                path += '('
                helper(path, ans, left + 1, right, n)
                path = path[0:len(path) - 1]
            if right < left:
                path += ')'
                helper(path, ans, left, right + 1, n)
                path = path[0:len(path) - 1]
        helper('', ans, 0, 0, n)
        return ans

solution = Solution()
print(solution.generateParenthesis(1))

# 思路：左括号比右括号多一定可以append右括号
