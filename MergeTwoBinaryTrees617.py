# Definition for a binary tree node.
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1 is None:
            return t2
        if t2 is None:
            return t1

        t1.val += t2.val

        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)
        return t1


node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)

node1.left = node2
node3.right = node4


def traverse(root):
    if root is None:
        return
    print(root.val)
    if root.left is not None:
        traverse(root.left)
    if root.right is not None:
        traverse(root.right)

solution = Solution()
node = solution.mergeTrees(node1, node3)
traverse(node)
