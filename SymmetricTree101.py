# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
        	return True
        return self.judge(root.left, root.right)

    def judge(self, root1, root2):
    	if root1 is None and root2 is None:
    		return True
    	if root1 is None and root2 is not None or root1 is not None and root2 is None:
    		return False
    	if root1.val != root2.val:
    		return False
    	return self.judge(root1.left, root2.right) and self.judge(root1.right, root2.left)


node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)

node1.left = node2
node1.right = node3

solution = Solution()
print(solution.isSymmetric(node1))