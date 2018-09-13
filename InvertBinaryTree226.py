# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
        	return root
        node = root.left 
        root.left = root.right
        root.right = node

        if root.left is not None:
        	self.invertTree(root.left)
        if root.right is not None:
        	self.invertTree(root.right)
        return root

solution = Solution()
node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)

node1.left = node2
node1.right = node3

solution.invertTree(node1)

print(node1.left.val)
print(node1.right.val)

