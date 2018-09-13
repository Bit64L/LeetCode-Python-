# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if root is None:
        	return []
        paths = []
        self.findPath(root, "", paths)
        return paths

    def findPath(self, root, path, paths):
        if root.left is None and root.right is None:
            paths.append(path + str(root.val))
            path = path + str(root.val) + "->"
            return
        path = path + str(root.val) + "->"
        if root.left is not None:
            self.findPath(root.left, path, paths)
        if root.right is not None:
            self.findPath(root.right, path, paths)


node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)

node1.left = node2
node1.right = node3
solution = Solution()
print(solution.binaryTreePaths(node1))