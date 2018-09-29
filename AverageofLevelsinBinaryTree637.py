# Definition for a binary tree node.
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        from Queue import Queue
        q = Queue()
        q.put(root)
        k, sum_, count = 1, 0, 1
        ans = []
        while q.qsize() != 0:
            node = q.get()
            sum_ += node.val
            k -= 1
            if node.left is not None:
                q.put(node.left)
            if node.right is not None:
                q.put(node.right)
            if k == 0:
                ans.append(sum_ / count)
                k = q.qsize()
                count = k
                sum_ = 0
        return ans
