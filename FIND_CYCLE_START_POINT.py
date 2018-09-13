class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
	def  detectCycle(self, head):
		if not head:
			return None
		fast = head
		slow = head
		while fast.next and fast.next.next:
			fast = fast.next.next
			slow = slow.next
			if fast == slow:
				break;
		if not fast.next or not fast.next.next:
			return None
		if fast == slow:
			slow = head
			while slow != fast:
				slow = slow.next
				fast = fast.next
			return slow
		return None


a=ListNode(0)
b=ListNode(1)
c=ListNode(2)
d=ListNode(3)
e=ListNode(4)
a.next = b
b.next = c
c.next = d 
d.next = e
e.next = c
solution = Solution()
node = solution.detectCycle(a)
print(node.val)




kwargs={}
kwargs['ha_on'] = False
ha_on = kwargs.get('', None)
print(ha_on)
if ha_on is None:
	print('None')
elif ha_on == True:
	print(True)
else:
	print('false or None')


extra_configs={}
extra_configs['ha_on'] = True
print(extra_configs.get('ha_on'))
print('123')
