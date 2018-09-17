# encoding=utf8
# Definition for a binary tree node.


class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def allPossibleFBT(self, N):
        """
        :type N: int
        :rtype: List[TreeNode]
        """
        if N % 2 == 0:
            return []
        candidates = [TreeNode(0) for i in range(N)]
        self.ans = []

        def helper(nodes, candidates):
            if len(candidates) == 0:
                tmp = list(nodes)
                self.ans.append(tmp[0])
                return
            for i in range(len(nodes)):
                if nodes[i].left is None and nodes[i].right is None:
                    nodes[i].left = candidates.pop()
                    nodes[i].right = candidates.pop()
                    nodes.append(nodes[i].left)
                    nodes.append(nodes[i].right)
                    helper(nodes, candidates)
                    nodes[i].left = None
                    nodes[i].right = None
                    candidates.append(nodes.pop())
                    candidates.append(nodes.pop())
        helper([candidates.pop()], candidates)
        return self.ans


solution = Solution()
ans = solution.allPossibleFBT(7)
print(len(ans))


# 注意：
# 1. [TreeNode(0) for i in range(N)] 和[TreeNode(0)] * N 的区别
#     后者生成的其实是同一个node的引用
