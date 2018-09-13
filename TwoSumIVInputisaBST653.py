# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def __init__(self):
        self.mark = False
        self.pocket = []

    def findTarget(self, root, k):
        if not root or (root.left is None and root.right is None):
            return False
        self.preTraverse(root, k)
        return self.mark

    def preTraverse(self, root, k):
        stack = []
        curr = root
        while True:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                if len(stack) == 0:
                    break
                curr = stack.pop()

                diff = k - curr.val
                if diff in self.pocket:
                    self.mark = True
                    return
                else:
                    self.pocket.append(curr.val)

                curr = curr.right

    def preTraverse2(self, root, k):
        if not root:
            return 
        if root.left:
            self.preTraverse2(root.left, k)

        diff = k - root.val
        if diff in self.pocket:
            self.mark = True
        else:
            self.pocket.append(root.val)

        if root.right:
            self.preTraverse2(root.right, k)







solution = Solution()
node1 = TreeNode(2)
node2 = TreeNode(1)
node3 = TreeNode(3)

node1.left = node2
node1.right = node3


# print(solution.preTraverse2(node1))
print(solution.findTarget(node1, 5))
