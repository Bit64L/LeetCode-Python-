# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
        	return 0
        queue = []
       	queue.append(root)
       	depth = 1
       	a = len(queue)
       	while len(queue) > 0:
       		if a == 0:
       			a = len(queue)
       			depth += 1
       		curr = queue.pop(0)
       		a -= 1
       		if curr.left is not None:
       			queue.append(curr.left)
       		if curr.right is not None:
       			queue.append(curr.right)
       	return depth
       		
node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)

node1.left = node2
node1.right = node3

solution = Solution()
print(solution.maxDepth(node1))