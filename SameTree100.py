# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        str1 = self.preTraverse(p)
        str2 = self.preTraverse(q)
        if str1 == str2:
            return True
        return False

    def preTraverse(self, root):
        curr, stack, str_ = root, [], ""
        while curr is not None or len(stack) > 0:
            if curr is not None:
                str_ += str(curr.val)
                stack.append(curr)
                curr = curr.left
            elif len(stack) > 0:
                str_ += "null"
                curr = stack.pop()
                curr = curr.right
        return str_


node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)

node1.left = node2
node2.right = node3

solution = Solution()
print(solution.isSameTree(node1, node2))






# class Solution:
#     def isSameTree(self, p, q):
#         """
#         :type p: TreeNode
#         :type q: TreeNode
#         :rtype: bool
#         """
#         if not p and not q:
#             return True
#         elif (not p and q) or (p and not q):
#             return False
#         else:
#             if p.val!=q.val:
#                 return False
#             else:
#                 return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
