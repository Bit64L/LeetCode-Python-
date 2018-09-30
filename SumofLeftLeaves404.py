# Definition for a binary tree node.
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.sum_ = 0

        def helper(root, mark):
            if root is None:
                return
            helper(root.left, 0)
            if root.left is None and root.right is None and mark == 0:
                self.sum_ += root.val
            helper(root.right, 1)
        helper(root, 1)
        return self.sum_

solution = Solution()
node1 = TreeNode(2)
node2 = TreeNode(1)
node3 = TreeNode(3)
node1.left = node2
node1.right = node3
print(solution.sumOfLeftLeaves(node1))
