class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        pPath = self.getPath(root, p)
        qPath = self.getPath(root, q)
        i = 0
        while i < (min(len(pPath), len(qPath))) and pPath[i] == qPath[i]:
            i = i + 1
        return qPath[i - 1]

    def getPath(self, root, node):
        path = []
        if root == node:
            return [root]
        while True:
            path.append(root)
            if node.val < root.val:
                root = root.left
            elif node.val > root.val:
                root = root.right
            elif node.val == root.val:
                path.append(node)
                break
        return path


n1 = TreeNode(2)
n2 = TreeNode(1)
n3 = TreeNode(3)

n1.left = n2
n1.right = n3

solution = Solution()
lca = solution.lowestCommonAncestor(n1, n2, n2)
print(lca.val)
