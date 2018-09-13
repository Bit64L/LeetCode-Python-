# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        vHead = ListNode(0)
        vHead.next = head
        count = 0
        p, q = vHead, vHead
        while q.next is not None:
        	if count >= n:
        		p = p.next
        	q = q.next
        	count += 1
        if p.next is not None:
        	p.next = p.next.next
        return vHead.next

solution = Solution()
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node1.next = node2
node2.next = node3
solution.removeNthFromEnd(node1, 2)

while node1 is not None:
	print(node1.val)
	node1= node1.next