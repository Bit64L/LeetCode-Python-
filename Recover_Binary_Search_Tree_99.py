from queue import Queue


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    pre = TreeNode(-99999)
    node1 = None
    node2 = None
    record = 0

    def recursion(self, root):
        if root.left is not None:
            self.recursion(root.left)
        if self.pre.val > root.val:
            if self.record == 0:
                self.node1 = self.pre
                self.node2 = root
                self.record = 1
            if self.record == 1:
                self.node2 = root
        self.pre = root
        if root.right is not None:
            self.recursion(root.right)

    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if root is None:
            return None
        self.recursion(root)
        if self.record != 0:
            tmp = self.node1.val
            self.node1.val = self.node2.val
            self.node2.val = tmp

    def output(self, root):
        if root is None:
            return
        if root.left is not None:
            self.output(root.left)
        print(root.val, end=" ")
        if root.right is not None:
            self.output(root.right)

    def layerTraverse(self, root):
        if root is None:
            return
        q = Queue()
        q.put(root)
        while not q.empty():
            node = q.get()
            print(node.val, end=" ")
            if node.left is not None:
                q.put(node.left)
            if node.right is not None:
                q.put(node.right)

n1 = TreeNode(1)
n2 = TreeNode(3)
n3 = TreeNode(2)

n1.left = n2
n2.right = n3

solution = Solution()

solution.output(n1)
print()
solution.recoverTree(n1)
solution.output(n1)

