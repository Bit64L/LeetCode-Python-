
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head):
        if not head:
            return False
        fast = head
        slow = head
        step = 0
        while fast and fast.next:
            step = step+1
            fast = fast.next.next
            slow = slow.next
            print(step)
            if fast == slow:
                return True
        return False

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
a.next = b
b.next = c
c.next = d
d.next = a
solutoin = Solution()
print(solutoin.hasCycle(a))