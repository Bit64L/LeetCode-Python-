# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution1:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # if root is None:
        # 	return True
        # left = self.getPath(root.left)
        # right = self.getPath(root.right)
        # if abs(left - right) > 1:
        # 	return False
        # return self.isBalanced(root.left) and self.isBalanced(root.right)
        if self.checkDepth(root) == -1:
        	return False
        return True

    def getPath(self, root):
    	if root is None:
    		return 0
    	return max(self.getPath(root.left), self.getPath(root.right)) + 1


    def checkDepth(self, root):

    	if root is None:
    		return True
    	left = self.checkDepth(root.left)
    	if left == -1:
    		return -1
    	right = self.checkDepth(root.right)
    	if right == -1:
    		return -1
    	if abs(left - right) > 1:
    		return -1
    	return max(left, right) + 1


class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if self.checkDepth(root) == -1:
        	return False
        return True


    def checkDepth(self, root):

    	if root is None:
    		return True
    	left = self.checkDepth(root.left)
    	if left == -1:
    		return -1
    	right = self.checkDepth(root.right)
    	if right == -1:
    		return -1
    	if abs(left - right) > 1:
    		return -1
    	return max(left, right) + 1



solution = Solution()
node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node1.left = node2
node2.right = node3
# print(solution.getPath(node1))
print(solution.isBalanced(node1))