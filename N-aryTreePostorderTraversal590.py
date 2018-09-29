"""
# Definition for a Node.
"""


class TreeNode(object):

    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution(object):

    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root:
            return []
        stack = [root]
        res = []
        while stack:
            node = stack.pop()
            res.append(node.val)
            for child in node.children:
                stack.append(child)
        return res[::-1]

    def postorder1(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        ans = []

        def helper(root, ans):
            if root is None:
                return
            if root.children is not None:
                for child in root.children:
                    helper(child, ans)
            ans.append(root.val)
        helper(root, ans)
        return ans

node2 = TreeNode(2, [])
node3 = TreeNode(3, [])
children = [node2, node3]
node1 = TreeNode(1, children)
solution = Solution()
print(solution.postorder(node1))
