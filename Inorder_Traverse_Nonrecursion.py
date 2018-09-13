class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    @classmethod
    def inorderTraverseNotRecursion(cls, root):
        if not root:
            return []
        curr = root
        stack = []
        while len(stack) > 0 or curr is not None:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                print(curr.val, end=' ')
                curr = curr.right


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(4)

solution = Solution()
solution.inorderTraverseNotRecursion(root)

