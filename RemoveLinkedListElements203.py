# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        curr = dummy
        while curr.next is not None:
        	if curr.next.val == val:
        		curr.next = curr.next.next
        	else:
        		curr = curr.next
        return dummy.next

node1 = ListNode(1)
node2 = ListNode(1)
node3 = ListNode(1)
node1.next = node2
node2.next = node3
solution = Solution()
head = solution.removeElements(node1, 1)
while head is not None:
	print(head.val)
	head = head.next
