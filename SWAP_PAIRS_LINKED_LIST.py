class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
	def swapPairs(self, head):
		if not head:
			return None
		if not head.next:
			return head
		curr = head
		after = head.next
		pre = None
		head = after
		while after:
			curr.next = after.next
			after.next = curr
			if pre:
				pre.next = after
			tmp = curr
			curr = after
			after = tmp
			
			if not after.next:
				break
			pre = curr.next
			curr = curr.next.next
			after = after.next.next
			print(pre.val)
		return head

solution = Solution()
a = ListNode(0)
b = ListNode(1)
c = ListNode(2)
d = ListNode(3)
a.next = b
b.next = c



x = solution.swapPairs(a)
while x:
	print(x.val)
	x = x.next