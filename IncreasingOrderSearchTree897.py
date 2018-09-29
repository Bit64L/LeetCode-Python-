# Definition for a binary tree node.
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.pre = None
        self.head = None

        def helper(root):
            if root is None:
                return
            if root.left is not None:
                helper(root.left)

            if self.pre is None:
                self.pre = root
                self.head = root
            else:
                root.left = None
                self.pre.right = root
                self.pre = root

            if root.right is not None:
                helper(root.right)
        helper(root)
        return self.head

node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node1.left = node2
# node1.right = node3
solution = Solution()
print(solution.increasingBST(node1))

# 注意点
# 当前结点的左子树要置None 否则TEL
