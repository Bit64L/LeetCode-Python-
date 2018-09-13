class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
	def reverseList(self, head):
		if not head:
			return None
		p = None
		while head:
			tmp = head
			head = head.next
			tmp.next = p
			p = tmp
		return p

solution = Solution()
a = ListNode(0)
b = ListNode(1)
c = ListNode(2)
a.next = b
b.next = c

x = solution.reverseList(a)
while x:
	print(x.val)
	x = x.next