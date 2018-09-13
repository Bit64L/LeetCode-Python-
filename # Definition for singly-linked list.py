# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
        	return head
        work = head 
        while work.next is not None:
        	if work.next.val == work.val:
        		work.next = work.next.next
        		continue
        	work = work.next
        return head

node1 = ListNode(1)
node2 = ListNode(1)
node3 = ListNode(3)

node1.next = node2
node2.next = node3

solution = Solution()
solution.deleteDuplicates(node1)

while node1 is not None:
	print(node1.val)
	node1 = node1.next