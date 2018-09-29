"""
# Definition for a Node.
"""


class TreeNode(object):

    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution(object):

    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        from Queue import Queue
        que = Queue()
        que.put(root)
        ans, tmp, k = [], [], 1
        while que.qsize() != 0:
            node = que.get()
            tmp.append(node.val)
            k -= 1
            for child in node.children:
                que.put(child)
            if k == 0:
                k = que.qsize()
                ans.append(list(tmp))
                tmp = []

        return ans

node2 = TreeNode(2, [])
node3 = TreeNode(3, [])
children = [node2, node3]
node1 = TreeNode(1, children)
solution = Solution()
print(solution.levelOrder(node1))
