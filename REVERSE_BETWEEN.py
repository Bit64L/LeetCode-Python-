class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
	def reverseBetween(self, head, m, n):
		if not head:
			return None
		vHead = ListNode(-1)
		vHead.next = head
		head = vHead
		first = head
		last = head
		while m + 1 > 2:
			first = first.next
			m = m - 1
		while n + 1 > 0:
			last = last.next
			n = n - 1
		sFirst = first.next
		curr = sFirst.next
		while curr != last:
			temp = curr
			curr = curr.next
			temp.next = sFirst
			sFirst = temp
		first.next.next = last
		first.next = sFirst
		return head.next

solution = Solution()
a = ListNode(0)
b = ListNode(1)
c = ListNode(2)
d = ListNode(3)
a.next = b
b.next = c
c.next = d

x = solution.reverseBetween(a, 1, 4)
while x:
	print(x.val)
	x = x.next


