"""
# Definition for a Node.
"""


class Node(object):

    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution(object):

    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if root is None:
            return 0
        from Queue import Queue
        q = Queue()
        q.put(root)
        k, ans = 0, 0
        while q.qsize() != 0:
            if k == 0:
                k = q.qsize()
                ans += 1
            node = q.get()
            k -= 1
            for child in node.children:
                q.put(child)
        return ans


node2 = Node(2, [])
node3 = Node(3, [])
children = [node2, node3]
node1 = Node(1, children)
solution = Solution()
print(solution.maxDepth(node1))
