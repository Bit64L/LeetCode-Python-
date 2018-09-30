# Definition for a binary tree node.
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0

        def helper(root):
            if root is None:
                return 0
            left = helper(root.left)
            right = helper(root.right)
            if self.ans < left + right:
                self.ans = left + right
            return max(left + 1, right + 1)
        helper(root)
        return self.ans
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
print(solution.diameterOfBinaryTree(node1))
