# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from fractions import gcd
class Solution(object):
    def insertGreatestCommonDivisors(self, head):
        if not head or not head.next:
            return head
        curr = head
        while curr and curr.next:
            kim = gcd(curr.val, curr.next.val)
            new_node = ListNode(kim)
            new_node.next = curr.next
            curr.next = new_node
            curr = curr.next.next
        return head
        
        