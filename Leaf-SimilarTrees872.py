# Definition for a binary tree node.
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        def helper(root, leaves):
            if root is None:
                return
            if root.left is None and root.right is None:
                leaves.append(root.val)
                return
            if root.left is not None:
                helper(root.left, leaves)
            if root.right is not None:
                helper(root.right, leaves)
        leaves1, leaves2 = [], []
        helper(root1, leaves1)
        helper(root2, leaves2)
        print(leaves1, leaves2)
        return leaves1 == leaves2

    def leafList(self, root):  # 参考：待返回值的递归
        if root is not None:
            if root.left is None and root.right is None:
                return [root.val]
            else:
                return self.leafList(root.left) + self.leafList(root.right)
        else:
            return []
node2 = TreeNode(2)
node3 = TreeNode(3)
node1 = TreeNode(1)
node1.left = node2
node1.right = node3
solution = Solution()
print(solution.leafSimilar(node1, node1))
