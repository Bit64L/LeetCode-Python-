# Definition for a binary tree node.
# encoding=utf8


class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        self.diff = 0

        def helper(root):
            if root is None:
                return 0
            left = helper(root.left)
            right = helper(root.right)
            self.diff += abs(left - right)
            return left + right + root.val

        helper(root)
        return self.diff


solution = Solution()
node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node1.left = node2
node1.right = node3
node2.left = node4
node3.left = node5
print(solution.findTilt(node1))

# 带返回值的递归
# 先想清楚递归函数的返回值代表什么意义
# 抽象使用函数
# 考虑返回值
# 注意递归出口，反之stack overflow
