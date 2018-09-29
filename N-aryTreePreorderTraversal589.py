"""
# Definition for a Node.
"""


class TreeNode(object):

    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution(object):

    def preorder(self, root):
        ans = []
        if root is None:
            return ans
        stack = []
        stack.append(root)
        while len(stack) != 0:
            tmp = stack.pop()
            ans.append(tmp.val)
            tmp.children.reverse()
            for child in tmp.children:
                stack.append(child)
        return ans

    def preorder1(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        ans = []

        def helper(root, ans):
            if root is None:
                return
            ans.append(root.val)
            for child in root.children:
                helper(child, ans)
        helper(root, ans)
        return ans


node2 = TreeNode(2, [])
node3 = TreeNode(3, [])
children = [node2, node3]
node1 = TreeNode(1, children)
solution = Solution()
print(solution.preorder(node1))
