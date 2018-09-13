
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
        if root is None:
            return None
        pParents = self.getParents(p, root)
        qParents = self.getParents(q, root)
        for pParent in pParents:
            for qParent in qParents:
                if pParent == qParent:
                    return pParent
        return None

    def getParents(self, node, root):
        parents = [node]
        while self.getParent(node, root) is not None:
            parents.append(self.getParent(node, root))
            node = self.getParent(node, root)
        return parents

    def getParent(self, node, root):
        if root is None:
            return
        q = [root]
        while len(q) > 0:
            tmp = q.pop(0)
            if tmp.left is not None:
                if tmp.left == node:
                    return tmp
                q.append(tmp.left)
            if tmp.right is not None:
                if tmp.right == node:
                    return tmp
                q.append(tmp.right)
        return None


def f(root, A, B):
    if root is None:
        return None
    if root.val == A.val or root.val == B.val:
        return root
    l = f(root.left, A, B)
    r = f(root.right, A, B)
    if l is not None and r is not None:
        return root
    elif l == r and r is not None:
        return None
    elif l is None:
        return r
    else:
        return l


n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)

n1.left = n2
n1.right = n3
n2.left = n4

solution = Solution()
lca = solution.lowestCommonAncestor(n1, n2, n4)
print(lca.val)

lca = f(n1, n2, n4)
print(lca.val)

