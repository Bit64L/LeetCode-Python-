# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.mark = True

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return

        self.check(root, root.val)

        if root.left is not None:
            self.isValidBST(root.left)
        if root.right is not None:
            self.isValidBST(root.right)

        return self.mark

    def check(self, root, val):
        if root is None:
            return

        if root.left is not None and root.left.val >= val:
            self.mark = False

        if root.right is not None and root.right.val <= val:
            self.mark = False

        self.check(root.left, val)
        self.check(root.right, val)


node1 = TreeNode(2)
node2 = TreeNode(1)
node3 = TreeNode(3)
node1.left = node2
node1.right = node3

solution = Solution()
print(solution.isValidBST(node1))
