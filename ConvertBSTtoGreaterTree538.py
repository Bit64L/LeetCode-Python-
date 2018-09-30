# Definition for a binary tree node.
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.pre = None

        def helper(root):
            if root is None:
                return
            helper(root.right)
            if self.pre is not None:
                root.val += self.pre.val
            self.pre = root
            helper(root.left)

        helper(root)
        return root

    def inTraverse(self, root):
        if root is None:
            return
        self.inTraverse(root.left)
        print(root.val)
        self.inTraverse(root.right)


solution = Solution()
node1 = TreeNode(2)
node2 = TreeNode(1)
node3 = TreeNode(3)
node1.left = node2
node1.right = node3
solution.convertBST(node1)
solution.inTraverse(node1)
# dynamic sum
