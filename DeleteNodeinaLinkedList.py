# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        while node.next is not None:
        	node.val = node.next.val
        	pre = node
        	node = node.next
        pre.next = None


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node1.next = node2
node2.next = node3
solution = Solution()
solution.deleteNode(node2)
while node1 is not None:
	print(node1.val)
	node1 = node1.next