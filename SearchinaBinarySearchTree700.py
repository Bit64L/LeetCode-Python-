# Definition for a binary tree node.
class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if root is None:
            return None
        if val == root.val:
            return root
        elif val < root.val:
            ans = self.searchBST(root.left, val)
        else:
            ans = self.searchBST(root.right, val)
        return ans

node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node1.left = node2
node1.right = node3
solution = Solution()
ans = solution.searchBST(node1, 4)
print(ans.val)
