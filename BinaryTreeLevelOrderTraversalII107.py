# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        curr = root
        queue = [curr]
        len_ = 1
        ans, temp_ans = [], []
        while len(queue) > 0:
            if len_ == 0:
                len_ = len(queue)
                ans.append(temp_ans)
                temp_ans = []
            curr = queue.pop(0)
            len_ -= 1
            temp_ans.append(curr.val)
            if curr.left is not None:
                queue.append(curr.left)
            if curr.right is not None:
                queue.append(curr.right)
        ans.append(temp_ans)
        ans.reverse()
        return ans


node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node1.left = node2
node1.right = node3
node3.right = node4
solution = Solution()
ans = solution.levelOrderBottom(node1)
for an in ans:
    print(an)
