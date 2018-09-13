# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# class Solution(object):
#     def getIntersectionNode(self, headA, headB):
#         """
#         :type head1, head1: ListNode
#         :rtype: ListNode
#         """
#         p, lenA = headA, 0
#         q, lenB = headB, 0
#         while p is not None:
#             lenA += 1
#             p = p.next
#         while q is not None:
#             lenB += 1
#             q = q.next
#         p, q = headA, headB
#         if lenA >= lenB:
#             for i in range(lenA - lenB):
#                 p = p.next
#         else:
#             for i in range(lenB - lenA):
#                 q = q.next
#         while q is not None and p is not None and p != q:
#             p = p.next
#             q = q.next
#         if p == q:
#             return p
#         return None
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        p, q = headA, headB
        while p != q:
            p = headB if p is None else p.next
            q = headA if q is None else q.next
        return p


solution = Solution()
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node1.next = node3
node2.next = node3
node = solution.getIntersectionNode(node1, node2)
print(node.val)
