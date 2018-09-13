# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        arr = []
        while head is not None:
        	arr.append(head.val)
        	head = head.next
        return arr == arr[::-1]

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(1)

node1.next = node2
node2.next = node3

solution = Solution()
print(solution.isPalindrome(node1))